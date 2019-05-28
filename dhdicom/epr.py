# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import pydicom
from dhdicom.exceptions import RegisterNotFound
from dhdicom.dicomi import DicomImage


class EPRData:

    def __init__(self, registers):
        self.registers = registers

    def anonimize(self, image):
        '''
        handler.anonimize(image) => dict: anonimiza los registros
        especificados durante la inicializacion de la imagen pasada por parámetros y devuelve los valores originales de estos registros en un diccionario donde las claves coindiden con los nombres de los registros.
        '''
        data = self.read(image)
        self._anonimize(image)
        return data

    def read(self, image):
        '''
        handler.read(image) => dict: devuelve los valores de los registros especificados durante la inicialización de la imagen pasada por
        parámetros en un diccionario donde las claves coinciden con los nombres
        de los registros.
        '''
        try:
            data = {
                register: str(getattr(image, register))
                for register in self.registers
            }
        except AttributeError:
            raise RegisterNotFound

        return data

    def _anonimize(self, image):
        for register in self.registers:
            setattr(image, register, 'pepe')
