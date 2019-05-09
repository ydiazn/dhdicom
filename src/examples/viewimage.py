
import numpy
import pydicom
from matplotlib import pyplot, cm

ds = pydicom.read_file("2.dcm")

dimensions = (
    int(ds.Rows),
    int(ds.Columns),
    1
)
spacing = (
    float(ds.PixelSpacing[0]),
    float(ds.PixelSpacing[1]),
    float(ds.SliceThickness)
)
x = numpy.arange(
    0.0,
    (dimensions[0] + 1) * spacing[0], spacing[0]
)
y = numpy.arange(
    0.0,
    (dimensions[1] + 1) * spacing[1], spacing[1]
)
z = numpy.arange(
    0.0,
    (dimensions[2] + 1) * spacing[2], spacing[2]
)
print(ds.pixel_array.dtype)
array = numpy.zeros(dimensions, dtype=ds.pixel_array.dtype)
array[:, :, 0] = ds.pixel_array

pyplot.figure(dpi=300)
pyplot.axes().set_aspect('equal', 'datalim')
pyplot.set_cmap(pyplot.gray())
pyplot.pcolormesh(x, y, numpy.flipud(array[:, :, 0]))
pyplot.show()
