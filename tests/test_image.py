# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-


import os
import unittest
from dhdicom.dicomi import DicomImage


class PropertiesTest(unittest.TestCase):

    def setUp(self):
        import pydicom

        filename = os.path.join(os.path.dirname(__file__), 'images/2.dcm')
        self.image = DicomImage(filename)
        self.ds = pydicom.read_file(filename)

    def test_dimensions(self):
        import pydicom

        dimensions = self.image.dimensions()
        self.assertTupleEqual(
            dimensions,
            (int(self.ds.Rows), int(self.ds.Columns))
        )

    def test_spacing(self):
        import pydicom

        spacing = self.image.spacing()
        self.assertTupleEqual(
            spacing,
            (
                float(self.ds.PixelSpacing[0]),
                float(self.ds.PixelSpacing[1]),
                float(self.ds.SliceThickness)
            )
        )


class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.image = DicomImage(
            os.path.join(os.path.dirname(__file__), 'images/2.dcm'))

    def test_get_register(self):
        self.assertEqual(
            self.image.PatientName,
            'FRANCISCO^ALVARES^QUESAD'
        )

    def test_set_register(self):
        self.image.PatientName = 'PepeJuan'
        self.assertEqual(
            self.image.PatientName,
            'PepeJuan'
        )


class PixelsTest(unittest.TestCase):

    def setUp(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'images/2.dcm')

    def test_read(self):
        import pydicom
        import numpy as np

        ds = pydicom.read_file(self.file_path)
        image = DicomImage(self.file_path)
        np.testing.assert_equal(
            ds.pixel_array,
            image.read()
        )

    # FIXME verificar la modificación de PixelData
    def test_set_pixels(self):
        import pydicom
        import numpy as np

        image = DicomImage(self.file_path)
        image.pixel_array[0][0] = 100
        image.write()
