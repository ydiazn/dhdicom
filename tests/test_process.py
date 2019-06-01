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

    def setUp(self):
        self.base = os.path.dirname(__file__)

    def test_authentic_image(self):
        from dhdicom.hidding.mixed import EPRHindingAndAuthentication

        filename = os.path.join(self.base, 'images/2.dcm')
        image = DicomImage(filename)

        registers = ['PatientName', 'PatientID']
        recipe = os.path.join(self.base, 'recipes/confidential')
        epr = EPRData(registers, recipe)
        hider = EPRHindingAndAuthentication('nuevaclave')

        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        new_image = handler.process(image)

        self.assertTrue(handler.authenticate(new_image))

    def test_not_authentic_image(self):
        from dhdicom.hidding.mixed import EPRHindingAndAuthentication
        import pydicom

        filename = os.path.join(self.base, 'images/2.dcm')
        image = DicomImage(filename)
        ds = pydicom.read_file(filename)

        dimesions = ds.Rows, ds.Columns

        registers = ['PatientName', 'PatientID']
        recipe = os.path.join(self.base, 'recipes/confidential')
        epr = EPRData(registers, recipe)
        hider = EPRHindingAndAuthentication('nuevaclave')

        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        new_image = handler.process(image)

        # Image Tampering
        x = dimesions[0] - 1
        y = dimesions[1] - 1
        new_image.pixel_array[0][0] += 1
        new_image.pixel_array[x][y] += 1
        new_image.write()

        # Despues del procesamiento los pixeles se modificaron
        authentic, blocks_tampered = handler.authenticate(new_image)
        self.assertFalse(authentic)
        # image size: 255x255, block size:32x32, block num: 255
        np.testing.assert_array_equal(
            blocks_tampered,
            np.array([0, 255])
        )

    def test_get_message(self):
        from dhdicom.hidding.mixed import EPRHindingAndAuthentication
        import pydicom

        filename = os.path.join(self.base, 'images/2.dcm')
        image = DicomImage(filename)
        ds = pydicom.read_file(filename)

        registers = ['PatientName', 'PatientID']
        patient_name = ds.PatientName
        patient_id = ds.PatientID

        recipe = os.path.join(self.base, 'recipes/confidential')
        epr = EPRData(registers, recipe)
        data = epr.read(image)
        hider = EPRHindingAndAuthentication('nuevaclave')

        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        new_image = handler.process(image)

        self.assertEqual(data, handler.get_epr(new_image))


if __name__ == '__main__':
    unittest.main()
