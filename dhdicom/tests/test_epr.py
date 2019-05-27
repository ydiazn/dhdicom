# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import os
import unittest
from dicomi import DicomImage
from dhdicom.epr import EPRData


class ReadEPRData(unittest.TestCase):

    def setUp(self):
        self.image = DicomImage(
            os.path.join(os.path.dirname(__file__), 'images/2.dcm'))

    def test_an_incorrect_register(self):
        from dhdicom.exceptions import RegisterNotFound

        registers = ['PatientName, PatientData']
        with self.assertRaises(RegisterNotFound) as context:
            handler = EPRData(registers)
            handler.read(self.image)

    def test_load_all_data_success(self):
        from dicomi import DicomImage

        registers = ['PatientName', 'PatientID']
        handler = EPRData(registers)
        data = handler.read(self.image)
        self.assertDictEqual(data,
            {
                'PatientName': 'FRANCISCO^ALVARES^QUESAD',
                'PatientID': 'HCMC-18-5456'
            },
            'Error extracting confidential data from image'
        )


class AnonimizeEPRData(unittest.TestCase):

    def setUp(self):
        self.image = DicomImage(
            os.path.join(os.path.dirname(__file__), 'images/2.dcm'))

    def test_an_incorrect_register(self):
        from dhdicom.exceptions import RegisterNotFound

        registers = ['PatientName, PatientData']
        with self.assertRaises(RegisterNotFound) as context:
            handler = EPRData(registers)
            handler.anonimize(self.image)

    def test_anonimize_success(self):
        from dicomi import DicomImage

        registers = ['PatientName', 'PatientID']
        handler = EPRData(registers)
        data = handler.anonimize(self.image)
        self.assertDictEqual(data,
            {
                'PatientName': 'FRANCISCO^ALVARES^QUESAD',
                'PatientID': 'HCMC-18-5456'
            },
            'Error extracting confidential data from image'
        )
        self.assertEqual(self.image.PatientName, 'pepe')
        self.assertEqual(self.image.PatientID, 'pepe')



