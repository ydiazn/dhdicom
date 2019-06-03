# -*- coding: utf-8 -*-
import os
import pydicom
import numpy as np
from dhdicom.dicomi import DicomImage
from dhdicom.hidding.mixed import EPRHindingAndAuthentication
from dhdicom.helpers.stego_metrics import Metrics
from dhdicom.helpers import utils
import imageio


def main():
    # Keys
    key = "Aslorent7N;fpr-y5"
    # Instance
    wm = EPRHindingAndAuthentication(key)
    base = os.path.dirname(__file__)
    image_file = os.path.join(base, 'images/2.dcm')
    image = DicomImage(image_file)
    cover_array = image.read()

    # Instances
    watermarked_image = wm.process(cover_array, 'Anier Soria Lorente')

    metr = Metrics()

    # Show metrics
    print(" Showing metrics")
    print("Experimental analysis")
    print(" ")
    print("PSNR: ", metr.psnr(cover_array, watermarked_image))
    print(" ")
    print("UIQI: ", metr.uiqi(cover_array, watermarked_image))
    print(" ")
    print("IF: ", metr.image_fid(cover_array, watermarked_image))
    print(" ")


if __name__ == '__main__':
    main()
