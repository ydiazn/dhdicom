# -*- coding: utf-8 -*-
import os
import numpy as np
from pylab import *
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt


def main():
    # Initial values
    # PSNR
    # j = 0
    # metr = "PSNR"
    # UIQI
    # j = 1
    # metr = "UIQI"
    # IF
    j = 2
    metr = "IF"
    # Keys
    key = "Aslorent7N;fpr-y5"

    # Creating directory
    dir = os.path.join(
        "dhdicom",
        "static",
        "Results"
    )
    if not os.path.exists(dir): os.makedirs(dir)

    try:
        root = Tk()
        filename = filedialog.askopenfilenames(
            parent=root, initialdir=dir, title='Please select a directory')
        # Load cover image (array)
        signal = np.loadtxt(filename[0])
    except Exception:
        raise ValueError("The image files were not loaded")

    root.destroy()

    plot(signal[:, j], '-o', ms=5, lw=2, alpha=0.7, mfc='red')
    axis([1, len(signal), amin(signal[:, j]), amax(signal[:, j])])
    xlabel('Images')
    ylabel(metr)
    title(metr + ' values')

    fig = plt.figure(1, figsize=(7, 7))
    # fig = plt.figure(1, figsize=(18, 7))

    plt.grid(True)

    # Creating dir of *.eps file
    direps = os.path.join(
        "dhdicom",
        "static",
        "Plots"
    )
    if not os.path.exists(direps): os.makedirs(direps)
    direps = os.path.join(
        direps,
        metr,
    )
    # Save the figures
    direps = "%s.jpg" % direps
    fig.savefig(direps)


if __name__ == '__main__':
    main()
