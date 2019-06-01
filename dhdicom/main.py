#!/usr/bin/python
# -*- coding: utf-8 -*-

# ~ import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *


import sys
# ~ from PyQt4 import QtGui


if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)


    # importar la ventana principal, es necesario el import aqui despues de
    # creada la QApplicarion
    from visual.principalUI import VentanaPrincipal

    # create widget
    w = VentanaPrincipal()
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())
