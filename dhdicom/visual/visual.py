# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Pruebas(object):
    def setupUi(self, Pruebas):
        Pruebas.setObjectName(_fromUtf8("Pruebas"))
        Pruebas.resize(651, 549)
        self.centralwidget = QtGui.QWidget(Pruebas)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea_3 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 350, 311, 111))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 309, 109))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 111, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_4 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_4.setGeometry(QtCore.QRect(330, 350, 311, 111))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 309, 109))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.btn_salir = QtGui.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(280, 470, 88, 29))
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.btn_procesar = QtGui.QPushButton(self.centralwidget)
        self.btn_procesar.setGeometry(QtCore.QRect(40, 300, 88, 29))
        self.btn_procesar.setObjectName(_fromUtf8("btn_procesar"))
        self.btn_analizar = QtGui.QPushButton(self.centralwidget)
        self.btn_analizar.setGeometry(QtCore.QRect(140, 300, 88, 29))
        self.btn_analizar.setObjectName(_fromUtf8("btn_analizar"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 611, 251))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.layout_original = QtGui.QHBoxLayout()
        self.layout_original.setObjectName(_fromUtf8("layout_original"))
        self.horizontalLayout_2.addLayout(self.layout_original)
        self.layout_procesada = QtGui.QHBoxLayout()
        self.layout_procesada.setObjectName(_fromUtf8("layout_procesada"))
        self.horizontalLayout_2.addLayout(self.layout_procesada)
        Pruebas.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Pruebas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuRuidos = QtGui.QMenu(self.menubar)
        self.menuRuidos.setObjectName(_fromUtf8("menuRuidos"))
        Pruebas.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Pruebas)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Pruebas.setStatusBar(self.statusbar)
        self.actionAbrir = QtGui.QAction(Pruebas)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionSalvar = QtGui.QAction(Pruebas)
        self.actionSalvar.setObjectName(_fromUtf8("actionSalvar"))
        self.actionCerrsar = QtGui.QAction(Pruebas)
        self.actionCerrsar.setObjectName(_fromUtf8("actionCerrsar"))
        self.actionRuido_1 = QtGui.QAction(Pruebas)
        self.actionRuido_1.setObjectName(_fromUtf8("actionRuido_1"))
        self.actionRuido_2 = QtGui.QAction(Pruebas)
        self.actionRuido_2.setObjectName(_fromUtf8("actionRuido_2"))
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionSalvar)
        self.menuRuidos.addAction(self.actionRuido_1)
        self.menuRuidos.addAction(self.actionRuido_2)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuRuidos.menuAction())

        self.retranslateUi(Pruebas)
        QtCore.QObject.connect(self.btn_salir, QtCore.SIGNAL(_fromUtf8("clicked()")), Pruebas.close)
        QtCore.QMetaObject.connectSlotsByName(Pruebas)

    def retranslateUi(self, Pruebas):
        Pruebas.setWindowTitle(_translate("Pruebas", "MainWindow", None))
        self.label_2.setText(_translate("Pruebas", "Id paciente:", None))
        self.label_3.setText(_translate("Pruebas", "Nombre paciente:", None))
        self.btn_salir.setText(_translate("Pruebas", "Salir", None))
        self.btn_procesar.setText(_translate("Pruebas", "Procesar", None))
        self.btn_analizar.setText(_translate("Pruebas", "Analizar", None))
        self.menuArchivo.setTitle(_translate("Pruebas", "Archivo", None))
        self.menuRuidos.setTitle(_translate("Pruebas", "Ruidos", None))
        self.actionAbrir.setText(_translate("Pruebas", "Abrir", None))
        self.actionSalvar.setText(_translate("Pruebas", "Salvar", None))
        self.actionCerrsar.setText(_translate("Pruebas", "Cerrar", None))
        self.actionRuido_1.setText(_translate("Pruebas", "Ruido 1", None))
        self.actionRuido_2.setText(_translate("Pruebas", "Ruido 2", None))

