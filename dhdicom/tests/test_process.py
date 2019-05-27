# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import os
import unittest
from dhdicom.processor import DHDicomHandler
from dhdicom.epr import EPRData
from dhdicom.dicomi import DicomImage


class ProcessTest(unittest.TestCase):

    def test_process(self):
        import numpy as np
        from dhdicom.hidding import DataHiding
        import pydicom

        filename = os.path.join(os.path.dirname(__file__), 'images/2.dcm')
        image = DicomImage(filename)
        dataset = pydicom.read_file(filename)

        patient_name = dataset.PatientName
        patient_id = dataset.PatientID
        pixels = dataset.pixel_array

        registers = ['PatientName', 'PatientID']
        epr = EPRData(registers)
        hider = DataHiding()

        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        handler.process(image)

        # Verificacion de la anonimizacion
        self.assertNotEqual(image.PatientName, patient_name)
        self.assertNotEqual(image.PatientID, patient_id)

        # Verificacion de los pixeles
        np.testing.assert_equal(image.read(), pixels)
