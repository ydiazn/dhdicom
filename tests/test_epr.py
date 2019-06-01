# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import os
import unittest
from dhdicom.dicomi import DicomImage
from dhdicom.epr import EPRData


class ReadEPRData(unittest.TestCase):

    def setUp(self):
        self.base = os.path.dirname(__file__)
        self.image = DicomImage(
            os.path.join(self.base, 'images/2.dcm'))

    def test_an_incorrect_register(self):
        from dhdicom.exceptions import RegisterNotFound

        registers = ['PatientName, PatientData']
        with self.assertRaises(RegisterNotFound) as context:
            recipe = os.path.join(self.base, 'recipes/confidential')
            handler = EPRData(registers, recipe)
            handler.read(self.image)

    def test_load_all_data_success(self):

        registers = ['PatientName', 'PatientID']
        recipe = os.path.join(self.base, 'recipes/confidential')
        handler = EPRData(registers, recipe)
        data = handler.read(self.image)
        self.assertDictEqual(
            data,
            {
                'PatientName': 'FRANCISCO^ALVARES^QUESAD',
                'PatientID': 'HCMC-18-5456'
            },
            'Error extracting confidential data from image'
        )


class AnonimizeEPRData(unittest.TestCase):

    def setUp(self):
        self.base = os.path.dirname(__file__)
        self.image = DicomImage(
            os.path.join(self.base, 'images/2.dcm'))

    def test_an_incorrect_register(self):
        from dhdicom.exceptions import RegisterNotFound

        registers = ['PatientName, PatientData']
        with self.assertRaises(RegisterNotFound) as context:
            recipe = os.path.join(self.base, 'recipes/confidential')
            handler = EPRData(registers, recipe)
            handler.anonimize(self.image)

    def test_anonimization_sucess(self):
        import pydicom

        registers = ['PatientName', 'PatientID']
        recipe = os.path.join(self.base, 'recipes/confidential')
        handler = EPRData(registers, recipe)

        # Verifica que efectivamente la imagen original tiene
        # los registros PatientName y PatientID
        self.image.PatientName
        self.image.PatientID

        file, data = handler.anonimize(self.image)

        # Verifica la eliminación de dichos registros tras la anonimización
        ds = pydicom.read_file(file)
        with self.assertRaises(AttributeError):
            ds.PatientName
        with self.assertRaises(AttributeError):
            ds.PatientID

        # Verificacion de los valores de los registros extraidos
        self.assertDictEqual(
            data,
            {
                'PatientName': 'FRANCISCO^ALVARES^QUESAD',
                'PatientID': 'HCMC-18-5456'
            },
            'Error extracting confidential data from image'
        )
