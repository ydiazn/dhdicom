#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
import json

import PyQt4
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pydicom
from matplotlib import pyplot, cm


from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.backends.backend_qt4agg import (
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from dhdicom.helpers.blocks_class import BlocksImage
from dhdicom.dicomi import DicomImage
from dhdicom.epr import EPRData

# cargar el visual
from .visual import Ui_Pruebas
import numpy as np
from dhdicom.processor import DHDicomHandler
from dhdicom.epr import EPRData
from dhdicom.hidding.mixed import EPRHindingAndAuthentication


# ventana principal de la aplicacion
class VentanaPrincipal(QMainWindow, Ui_Pruebas):
    def __init__(self, parent=None):
        # inicializar el padre
        super(VentanaPrincipal, self).__init__(parent)
        # configurar la interfaz
        self.setupUi(self)

        self.original_image = None
        self.watermarked_image = None
        self. actionAbrir.triggered.connect(self.Cargar_imagen)
        self. actionSalvar.triggered.connect(self.Salvar_imagen)
        self.btn_procesar.clicked.connect(self.Procesar_imagen)
        self.btnExtractAuthenticate.clicked.connect(self.analizar)
        self.init_canvas()

        # Registros EPR
        base = os.path.dirname(os.path.dirname(__file__))
        self.epr = EPRData(
            ['PatientID', 'PatientName'],
            os.path.join(base, 'recipes/confidential')
        )
        self.hider = EPRHindingAndAuthentication('nuevaclave')

    def Cargar_imagen(self):
        ruta_imagen = QFileDialog.getOpenFileName(
            self, u"Cargar Imágenes", QDir.homePath(), u"Imágenes (*.dcm)")
        self.clear_canvas()

        self.original_image = DicomImage(ruta_imagen)
        self.draw_image(self.dicom_canvas, self.original_image)
        data = self.epr.read(self.original_image)
        self.load_epr_data(data)

    def load_epr_data(self, data):
        patient_id = data['PatientID'] or 'undefinied'
        patient_name = data['PatientName'] or 'undefinied'
        self.lb_paciente_id.setText(patient_id)
        self.lb_paciente_name.setText(patient_name)

    def load_epr_hidden(self, data):
        patient_id = data['PatientID'] or 'undefinied'
        patient_name = data['PatientName'] or 'undefinied'
        self.lb_paciente_id_oculto.setText(patient_id)
        self.lb_paciente_name_oculto.setText(patient_name)

    def init_canvas(self):
        pyplot.set_cmap(pyplot.gray())
        # Original image
        figure = Figure()
        ax = figure.add_subplot(111)
        ax.set_aspect('equal', 'datalim')
        self.dicom_canvas = FigureCanvas(figure)

        # Watermarking image
        figure = Figure()
        ax = figure.add_subplot(111)
        ax.set_aspect('equal', 'datalim')
        self.watermarked_canvas = FigureCanvas(figure)

        self.canvasLayout.addWidget(self.dicom_canvas)
        self.canvasLayout.addWidget(self.watermarked_canvas)

    def draw_image(self, canvas, image):
        figure = canvas.figure
        ax = figure.get_axes()[0]

        dimensions = (
            int(image.Rows),
            int(image.Columns)
        )
        spacing = (
            float(image.PixelSpacing[0]),
            float(image.PixelSpacing[1]),
            float(image.SliceThickness)
        )
        x = np.arange(
            0.0,
            (dimensions[0] + 1) * spacing[0], spacing[0]
        )
        y = np.arange(
            0.0,
            (dimensions[1] + 1) * spacing[1], spacing[1]
        )
        z = np.arange(
            0.0,
            2 * spacing[2], spacing[2]
        )

        ax.set_aspect('equal', 'datalim')
        ax.pcolormesh(x, y, np.flipud(image.read()))
        canvas.draw()

    def Procesar_imagen(self):
        handler = DHDicomHandler(
            data_handler=self.epr, hider_handler=self.hider)
        image = handler.process(self.original_image)
        self.draw_image(self.watermarked_canvas, image)
        self.load_epr_data(self.epr.read(image))
        self.load_epr_hidden(handler.get_epr(image))
        self.watermarked_image = image

    def Salvar_imagen(self):
        dirName = QFileDialog.getExistingDirectory(
            self,
            u"Seleccionar ubicación",
            QDir.homePath(),
            QFileDialog.ShowDirsOnly
        )
        nombre = QInputDialog.getText(
            self,
            u"Nombre de la imagen",
            u"Escriba el nombre de la imagen",
            text="dhdicom"
        )
        dir_imagen_guardada = '{}/{}.dcm'.format(dirName, nombre[0])
        self.watermarked_image.save(dir_imagen_guardada)

    def analizar(self):
        handler = DHDicomHandler(
            data_handler=self.epr, hider_handler=self.hider)
        try:
            data = handler.get_epr(self.original_image)
            self.load_epr_hidden(data)
        except json.JSONDecodeError:
            self.load_epr_hidden({
                'PatientName': None,
                'PatientID': None
            })

        self.draw_image(self.watermarked_canvas, self.original_image)

    def clear_canvas(self):
        self.lb_paciente_id_oculto.setText('')
        self.lb_paciente_name_oculto.setText('')
        self.lb_paciente_id.setText('')
        self.lb_paciente_name.setText('')

        self.watermarked_canvas.figure.get_axes()[0].clear()
        self.watermarked_canvas.draw()
        self.dicom_canvas.figure.get_axes()[0].clear()
        self.dicom_canvas.draw()
