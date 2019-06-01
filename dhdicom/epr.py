# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import pydicom
from dhdicom.exceptions import RegisterNotFound
from dhdicom.dicomi import DicomImage
from deid.dicom import replace_identifiers
from deid.dicom import get_identifiers
from deid.config import DeidRecipe


class EPRData:

    def __init__(self, registers, recipe_file):
        self.registers = registers
        self.recipe = DeidRecipe(deid=recipe_file)

    def anonimize(self, image):
        '''
        handler.anonimize(image) => tuple: anonimiza los registros
        especificados durante la inicializacion de la imagen pasada
        por parámetros. Devuelve la ruta de un fichero temporal que contiene
        la imagen anonimizada y los registros originales en un diccionario.
        '''
        data = self.read(image)
        file = self._anonimize(image)
        return file, data

    def read(self, image):
        '''
        handler.read(image) => dict: devuelve los valores de los registros
        especificados durante la inicialización de la imagen pasada por
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
        '''
        self._anonimize(image) => file path, anonimiza la imagen pasada
        por parámetros según las reglas definidas en self.recipe y devuelve
        la ruta de un fichero temporal con dichas modificaciones
        '''
        files = [image.path]
        ids = get_identifiers(files)
        cleaned_files = replace_identifiers(
            dicom_files=files, deid=self.recipe, ids=ids)
        return cleaned_files[0]
