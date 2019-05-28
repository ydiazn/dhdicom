# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import pydicom
from dhdicom.exceptions import RegisterNotFound


class DicomImage():

    def __init__(self, image_path):
        self.image_path = image_path
        self.ds = pydicom.read_file(image_path)

    def __getattr__(self, attr):
        return getattr(self.ds, attr)

    def read(self):
        '''
        image.read() => numpy array: Devuelve los píxeles de la imagen
        '''
        return self.ds.pixel_array

    def write(self):
        '''
        image.write(pixels): Establece los pixels de la imagen dicom
        '''
        self.ds.PixelData = self.ds.pixel_array.tobytes()

    def dimensions(self):
        return (int(self.Rows), int(self.Columns))

    def spacing(self):
        return (
            float(self.PixelSpacing[0]),
            float(self.PixelSpacing[1]),
            float(self.SliceThickness)
        )
