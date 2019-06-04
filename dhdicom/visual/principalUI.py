#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

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


# ventana principal de la aplicacion
class VentanaPrincipal(QMainWindow, Ui_Pruebas):
    def __init__(self, parent=None):
        # inicializar el padre
        super(VentanaPrincipal, self).__init__(parent)
        # configurar la interfaz
        self.setupUi(self)

        self.original_image = None
        self. actionAbrir.triggered.connect(self.Cargar_imagen)
        self. actionSalvar.triggered.connect(self.Salvar_imagen)
        self.btn_procesar.clicked.connect(self.Procesar_imagen)
        self.init_canvas()
        self.epr = EPRData(['PatientID', 'PatientName'])

    def Cargar_imagen(self):
        ruta_imagen = QFileDialog.getOpenFileName(
            self, u"Cargar Imágenes", QDir.homePath(), u"Imágenes (*.dcm)")

        self.original_image = DicomImage(ruta_imagen)
        self.draw_image(self.dicom_canvas, self.original_image)
        self.load_epr_data(self.original_image)

    def load_epr_data(self, image):
        data = self.epr.read(image)
        self.lb_paciente_id.setText(data['PatientID'])
        self.lb_paciente_name.setText(data['PatientName'])

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
        self.draw_image(self.watermarked_canvas, self.original_image)

    def Salvar_imagen(self):
        pass
