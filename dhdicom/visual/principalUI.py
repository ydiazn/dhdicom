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
from matplotlib.patches import Rectangle
from dhdicom.helpers.blocks_class import BlocksImage
from dhdicom.dicomi import DicomImage
from dhdicom.epr import EPRData

# cargar el visual
from .visual import Ui_Pruebas
import numpy as np
from dhdicom.processor import DHDicomHandler
from dhdicom.epr import EPRData
from dhdicom.hidding.mixed import EPRHindingAndAuthentication
from dhdicom.helpers.blocks_class import BlocksImage
from dhdicom.helpers.utils import cropping_noise, random_list
from dhdicom import settings


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
        self. actionCropping.triggered.connect(self.crop_image)
        self.btn_procesar.clicked.connect(self.Procesar_imagen)
        self.btnExtractAuthenticate.clicked.connect(self.analizar)
        self.init_canvas()

        # Registros EPR
        base = os.path.dirname(os.path.dirname(__file__))
        self.epr = EPRData(settings.EPR_TO_HIDE, settings.RECIPE_FILE)
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
        ax.clear()
        ax.imshow(image.read())
        canvas.draw()

    def Procesar_imagen(self):
        ouput = QInputDialog.getText(
            self,
            u"Hiding EPR",
            u"Enter a password",
            text=""
        )
        clave = ouput[0]
        hider = EPRHindingAndAuthentication(clave)
        handler = DHDicomHandler(
            data_handler=self.epr, hider_handler=hider)
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
        output = QInputDialog.getText(
            self,
            u"Hiding EPR",
            u"Enter a password",
            text=""
        )
        clave = output[0]
        hider = EPRHindingAndAuthentication(clave)
        self.draw_image(self.watermarked_canvas, self.original_image)

        handler = DHDicomHandler(
            data_handler=self.epr, hider_handler=hider)

        # Tamper dectection
        authentic, *l = handler.authenticate(self.original_image)

        if not authentic:
            block_manager = BlocksImage(self.original_image.read(), 32, 32)
            total_blocks = block_manager.max_num_blocks()
            modified_blocks = l[0]
            if modified_blocks:
                self.draw_tamper_regions(modified_blocks)
            image_modification = len(modified_blocks) / total_blocks

            if image_modification > 0.9:
                message = "Image is not authentic or its " \
                    "authenticity could not to be verified. " \
                    "View tamper region in right image. " \
                    "Make sure the password is correct."
            else:
                message = "Image is not authentic." \
                    "View tamper region in right image."
        else:
            message = "Image is authentic."

        QMessageBox.information(
                self,
                u"Image authentication",
                message,
            )

        # Extraccion del EPR
        try:
            data = handler.get_epr(self.original_image)
            self.load_epr_hidden(data)
        except json.JSONDecodeError:
            self.load_epr_hidden({
                'PatientName': None,
                'PatientID': None
            })

    def clear_canvas(self):
        self.lb_paciente_id_oculto.setText('')
        self.lb_paciente_name_oculto.setText('')
        self.lb_paciente_id.setText('')
        self.lb_paciente_name.setText('')

        self.watermarked_canvas.figure.get_axes()[0].clear()
        self.watermarked_canvas.draw()
        self.dicom_canvas.figure.get_axes()[0].clear()
        self.dicom_canvas.draw()

    def crop_image(self):
        x0, p, n = 0.47, 0.27, 15
        z_block = [16, 32, 64]
        cover_array = np.copy(self.original_image.read())
        # Selected blocks
        for i in range(n):
            # Instance
            j = z_block[i % 3]
            if len(cover_array.shape) == 2:
                blocks_instance = BlocksImage(cover_array, j, j)
                L = random_list(
                    x0, p, list(range(blocks_instance.max_num_blocks())))
                blocks_instance.set_block(cropping_noise(
                    blocks_instance.get_block(L[i]), j, j), L[i]
                )
            else:
                blocks_instance = BlocksImage3D(cover_array, j, j)
                L = random_list(
                    x0, p, list(range(blocks_instance.max_num_blocks_image_3d())))
                blocks_instance.set_block_image_3d(cropping_noise(
                    blocks_instance.get_block_image_3d(L[i]), j, j), L[i]
                )
        self.original_image.write(cover_array)
        self.draw_image(self.dicom_canvas, self.original_image)

    def draw_tamper_regions(self, block_indexes):
        block_image = BlocksImage(self.original_image.read(), 32, 32)
        figure = self.watermarked_canvas.figure
        ax = figure.get_axes()[0]

        block_width = 32
        block_height = 32

        for block_index in block_indexes:
            coords = block_image.get_coord(block_index)
            x = coords[2]
            y = coords[0]

            rect = Rectangle(
                (x, y), block_width, block_height,
                linewidth=1,
                edgecolor='r',
                facecolor='none'
            )
            ax.add_patch(rect)
        self.watermarked_canvas.draw()
