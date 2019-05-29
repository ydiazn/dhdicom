
import numpy as np
import pydicom
from matplotlib import pyplot, cm
import os

base_dir = os.path.dirname(__file__)
filename = os.path.join(base_dir, 'images/1.dcm')
ds = pydicom.read_file(filename)

dimensions = (
    int(ds.Rows),
    int(ds.Columns)
)
spacing = (
    float(ds.PixelSpacing[0]),
    float(ds.PixelSpacing[1]),
    float(ds.SliceThickness)
)
x = np.arange(
    0.0,
    (dimensions[0] + 1) * spacing[0], spacing[0]
)
y = np.arange(
    0.0,
    (dimensions[1] + 1) * spacing[1], spacing[1]
)
z = np.arange(
    0.0,
    2 * spacing[2], spacing[2]
)

pyplot.figure(dpi=300)
pyplot.axes().set_aspect('equal', 'datalim')
pyplot.set_cmap(pyplot.gray())
pyplot.pcolormesh(x, y, np.flipud(ds.pixel_array))
pyplot.show()
