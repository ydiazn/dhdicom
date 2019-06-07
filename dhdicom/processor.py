# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import json
import numpy as np
from dhdicom.dicomi import DicomImage


class DHDicomHandler:

    def __init__(self, data_handler=None, hider_handler=None):
        self.data_handler = data_handler
        self.hider_handler = hider_handler

    def process(self, image):
        '''
        handler.process(image), oculta registros del EPR en la imagen y
        los anonimiza. Los registros se especifican en el data_handler
        '''

        # anonimización
        file, epr = self.data_handler.anonimize(image)
        # Ocultacion del EPR y autenticacion
        new_image = DicomImage(file)
        msg = json.dumps(epr)
        data = new_image.read()
        watermarked_pixels = self.hider_handler.process(
            data, msg)
        new_image.write(watermarked_pixels)
        return new_image

    def authenticate(self, image):
        return self.hider_handler.authenticate(image.read())

    def get_epr(self, image):
        pixels = image.read()
        msg = self.hider_handler.get_msg(pixels)
        return json.loads(msg)
