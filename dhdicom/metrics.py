# -*- coding: utf-8 -*-
import os
import pydicom
import numpy as np
from tkinter import *
from tkinter import filedialog
from dhdicom.epr import EPRData
from dhdicom.helpers import utils
from dhdicom.dicomi import DicomImage
from dhdicom.processor import DHDicomHandler
from dhdicom.helpers.stego_metrics import Metrics
from dhdicom.hidding.mixed import EPRHindingAndAuthentication


def main():
    # Keys
    key = "Aslorent7N;fpr-y5"

    base = os.path.dirname(__file__)

    # Directory
    dir = "tests/dicom"
    if not os.path.exists(dir): os.makedirs(dir)

    try:
        root = Tk()
        filename = filedialog.askopenfilenames(
            parent=root, initialdir=dir, title='Please select a directory')
        # Load cover image (array)
        cover = DicomImage(filename[0])
    except Exception:
        raise ValueError("The image files were not loaded")

    root.destroy()

    # Creating matrix
    M_Metrics = []

    # Creating directory
    dir_dat_file = os.path.join(
        "dhdicom",
        "static",
        "Results"
    )
    if not os.path.exists(dir_dat_file): os.makedirs(dir_dat_file)
    dir_dat_file = os.path.join(
        dir_dat_file,
        filename[0].split("/")[-2]
    )
    dir_dat_file = "%s_Results.dat" % dir_dat_file

    # Instance
    metr = Metrics()

    # Building stego images. Generating results
    for i in range(len(filename)):
        row = []
        # Generating keys
        key = utils.sha256_to_key_bin(key)
        image = DicomImage(filename[i])
        registers = ['PatientName', 'PatientID']
        recipe = os.path.join(base, 'recipes/confidential')
        epr = EPRData(registers, recipe)
        hider = EPRHindingAndAuthentication(key)
        handler = DHDicomHandler(data_handler=epr, hider_handler=hider)
        new_image = handler.process(image)
        cover_array = image.read()
        watermarked_array = new_image.read()
        # Experimental analysis
        row.append(metr.psnr(cover_array, watermarked_array))
        row.append(metr.uiqi(cover_array, watermarked_array))
        row.append(metr.image_fid(cover_array, watermarked_array))
        print(" ")
        print("Experimental analysis")
        print(" ")
        print("PSNR: ", row[0])
        print(" ")
        print("UIQI: ", row[1])
        print(" ")
        print("IF: ", row[2])
        print(" ")
        # Creating cols
        M_Metrics.append(row)
        # Saving results
        np.savetxt(dir_dat_file, M_Metrics, fmt="%.9e")

    # Saving results
    np.savetxt(dir_dat_file, M_Metrics, fmt="%.9e")


if __name__ == '__main__':
    main()
