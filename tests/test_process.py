# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import os
import unittest
import pydicom
import numpy as np
from dhdicom.processor import DHDicomHandler
from dhdicom.epr import EPRData
from dhdicom.dicomi import DicomImage


class ProcessTest(unittest.TestCase):
    def test_process(self):
        from dhdicom.hidding.mixed import EPRHindingAndAuthentication

        filename = os.path.join(os.path.dirname(__file__), 'images/2.dcm')
        image = DicomImage(filename)
        dataset = pydicom.read_file(filename)

        patient_name = dataset.PatientName
        patient_id = dataset.PatientID
        pixels = np.copy(dataset.pixel_array)

        registers = ['PatientName', 'PatientID']
        epr = EPRData(registers)
        hider = EPRHindingAndAuthentication('nuevaclave')

        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        handler.process(image)

        # Verificacion de la anonimizacion
        self.assertNotEqual(image.PatientName, patient_name)
        self.assertNotEqual(image.PatientID, patient_id)

        # Despues del procesamiento los pixeles se modificaron
        np.testing.assert_raises(
            AssertionError, np.testing.assert_array_equal, image.read(), pixels
        )

    def test_authentic_image(self):
        from dhdicom.hidding.mixed import EPRHindingAndAuthentication

        filename = os.path.join(os.path.dirname(__file__), 'images/2.dcm')
        image = DicomImage(filename)

        registers = ['PatientName', 'PatientID']
        epr = EPRData(registers)
        hider = EPRHindingAndAuthentication('nuevaclave')

        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        handler.process(image)

        # Despues del procesamiento los pixeles se modificaron
        self.assertTrue(handler.authenticate(image))

    def test_not_authentic_image(self):
        from dhdicom.hidding.mixed import EPRHindingAndAuthentication
        import pydicom

        filename = os.path.join(os.path.dirname(__file__), 'images/2.dcm')
        image = DicomImage(filename)
        ds = pydicom.read_file(filename)

        dimesions = ds.Rows, ds.Columns

        registers = ['PatientName', 'PatientID']
        epr = EPRData(registers)
        hider = EPRHindingAndAuthentication('nuevaclave')

        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        handler.process(image)

        # Image Tampering
        x = dimesions[0] - 1
        y = dimesions[1] - 1
        image.pixel_array[0][0] += 1
        image.pixel_array[x][y] += 1
        image.write()

        # Despues del procesamiento los pixeles se modificaron
        authentic, blocks_tampered = handler.authenticate(image)
        self.assertFalse(authentic)
        # image size: 255x255, block size:32x32, block num: 255
        np.testing.assert_array_equal(
            blocks_tampered,
            np.array([0, 255])
        )


if __name__ == '__main__':
    unittest.main()
