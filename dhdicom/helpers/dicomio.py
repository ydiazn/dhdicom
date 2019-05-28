import os
import pydicom
import imageio


class ImagenIO:
    @staticmethod
    def get_class(file):
        if os.path.splitext(file)[1] == ".dcm":
            return DicomIO
        else:
            return ImageIO

    @classmethod
    def read(cls, file):
        io_class = cls.get_class(file)
        return io_class.read(file)

    @classmethod
    def save(cls, file, data, **kwargs):
        io_class = cls.get_class(file)
        io_class.save(file, data, **kwargs)


class ImageIO:

    @staticmethod
    def read(file):
        return imageio.imread(file)

    @staticmethod
    def save(file, data, **kwargs):
        imageio.imsave(file, data)


class DicomIO:

    @staticmethod
    def read(file):
        ds = pydicom.read_file(file)
        return ds.pixel_array

    @staticmethod
    def save(file, data, original=None):
        ds = pydicom.read_file(original)
        ds.PixelData = data.tobytes()
        ds.save_as(file)


def read(file):
    return ImagenIO.read(file)


def save(file, data, **kwargs):
    return ImagenIO.save(file, data, **kwargs)
