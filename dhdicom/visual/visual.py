# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dhdicom/visual/untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Pruebas.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Pruebas)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.canvasLayout = QtGui.QHBoxLayout()
        self.canvasLayout.setObjectName(_fromUtf8("canvasLayout"))
        self.verticalLayout_4.addLayout(self.canvasLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.scrollArea_3 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 381, 187))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.formLayout = QtGui.QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lb_paciente_id = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.lb_paciente_id.setText(_fromUtf8(""))
        self.lb_paciente_id.setObjectName(_fromUtf8("lb_paciente_id"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lb_paciente_id)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lb_paciente_name = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.lb_paciente_name.setText(_fromUtf8(""))
        self.lb_paciente_name.setObjectName(_fromUtf8("lb_paciente_name"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lb_paciente_name)
        self.label_3.raise_()
        self.lb_paciente_name.raise_()
        self.label_2.raise_()
        self.lb_paciente_id.raise_()
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.scrollArea_4 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 381, 187))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.formLayout_2 = QtGui.QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lb_paciente_id_oculto = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.lb_paciente_id_oculto.setText(_fromUtf8(""))
        self.lb_paciente_id_oculto.setObjectName(_fromUtf8("lb_paciente_id_oculto"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lb_paciente_id_oculto)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lb_paciente_name_oculto = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.lb_paciente_name_oculto.setText(_fromUtf8(""))
        self.lb_paciente_name_oculto.setObjectName(_fromUtf8("lb_paciente_name_oculto"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lb_paciente_name_oculto)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout.addWidget(self.scrollArea_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_procesar = QtGui.QPushButton(self.centralwidget)
        self.btn_procesar.setObjectName(_fromUtf8("btn_procesar"))
        self.horizontalLayout_3.addWidget(self.btn_procesar)
        self.btn_analizar = QtGui.QPushButton(self.centralwidget)
        self.btn_analizar.setObjectName(_fromUtf8("btn_analizar"))
        self.horizontalLayout_3.addWidget(self.btn_analizar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.scrollArea_3.raise_()
        self.scrollArea_4.raise_()
        self.btn_procesar.raise_()
        self.btn_analizar.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        Pruebas.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Pruebas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.actionRuidoSalPimienta = QtGui.QAction(Pruebas)
        self.actionRuidoSalPimienta.setObjectName(_fromUtf8("actionRuidoSalPimienta"))
        self.actionRuido_2 = QtGui.QAction(Pruebas)
        self.actionRuido_2.setObjectName(_fromUtf8("actionRuido_2"))
        self.actionCropping = QtGui.QAction(Pruebas)
        self.actionCropping.setObjectName(_fromUtf8("actionCropping"))
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionSalvar)
        self.menuRuidos.addAction(self.actionRuidoSalPimienta)
        self.menuRuidos.addAction(self.actionRuido_2)
        self.menuRuidos.addAction(self.actionCropping)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuRuidos.menuAction())

        self.retranslateUi(Pruebas)
        QtCore.QMetaObject.connectSlotsByName(Pruebas)

    def retranslateUi(self, Pruebas):
        Pruebas.setWindowTitle(_translate("Pruebas", "MainWindow", None))
        self.label_5.setText(_translate("Pruebas", "Datos confidenciales", None))
        self.label_6.setText(_translate("Pruebas", "Cabecera del DICOM", None))
        self.label_2.setText(_translate("Pruebas", "ID:", None))
        self.label_3.setText(_translate("Pruebas", "Nombre:", None))
        self.label_7.setText(_translate("Pruebas", "Oculto en la imagen", None))
        self.label.setText(_translate("Pruebas", "ID:", None))
        self.label_4.setText(_translate("Pruebas", "Nombre:", None))
        self.btn_procesar.setText(_translate("Pruebas", "Procesar", None))
        self.btn_analizar.setText(_translate("Pruebas", "Analizar", None))
        self.menuArchivo.setTitle(_translate("Pruebas", "Archivo", None))
        self.menuRuidos.setTitle(_translate("Pruebas", "Ruidos", None))
        self.actionAbrir.setText(_translate("Pruebas", "Abrir", None))
        self.actionSalvar.setText(_translate("Pruebas", "Salvar", None))
        self.actionCerrsar.setText(_translate("Pruebas", "Cerrar", None))
        self.actionRuidoSalPimienta.setText(_translate("Pruebas", "Sal y pimienta", None))
        self.actionRuido_2.setText(_translate("Pruebas", "Gausiano", None))
        self.actionCropping.setText(_translate("Pruebas", "Cropping", None))

