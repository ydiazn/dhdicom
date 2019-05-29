#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

import PyQt4
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pydicom
from matplotlib import pyplot, cm



from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# cargar el visual
from .visual import Ui_Pruebas
import numpy as np


# ventana principal de la aplicacion
class VentanaPrincipal(QMainWindow, Ui_Pruebas):
	def __init__(self, parent = None):
		# inicializar el padre
		super(VentanaPrincipal, self).__init__(parent)
		# configurar la interfaz
		self.setupUi(self)
		
		self.ruta_imagen=None
		
		
		
		self. actionAbrir.triggered.connect(self.Cargar_imagen)
		self. actionSalvar.triggered.connect(self.Salvar_imagen)
		
		self.btn_procesar.clicked.connect(self.Procesar_imagen)
		
		
	def Cargar_imagen(self):
		self.ruta_imagen = QFileDialog.getOpenFileName(self, u"Cargar Imágenes", QDir.homePath(), u"Imágenes (*.dcm)")
		

		
		self.figure = Figure()
		self.canvas = FigureCanvas(self.figure)
		self.layout_original.addWidget(self.canvas)

		ax = self.figure.add_subplot(111)
		
		ds = pydicom.read_file(self.ruta_imagen)

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

		ax.set_aspect('equal', 'datalim')
		pyplot.set_cmap(pyplot.gray())
		ax.pcolormesh(x, y, np.flipud(ds.pixel_array))
		
		
		
		self.canvas.draw()
	
	
	def Procesar_imagen(self):
		import random


		
		self.figure = Figure()
		self.canvas = FigureCanvas(self.figure)
		self.layout_original.addWidget(self.canvas)
		x= np.linspace(0, 50)
		y= np.sin(x)
		ax = self.figure.add_subplot(111)
		ax.plot(x,y)
		self.canvas.draw()
		
		
		
        
		
	def Salvar_imagen(self):
		
		
		#~ self.showFullScreen()
		
		'''
		#para la conexion a la bd de articulos
		self.__con = lite.connect('base_datos/articulos.db')
		self.__cursor = self.__con.cursor()
		
		
		#para la conexion a la bd de ventas
		self.__con1 = lite.connect('base_datos/ventas.db')
		self.__cursor1 = self.__con1.cursor()
		
		
		#para la conexion a la bd de devoluciones
		self.__con2 = lite.connect('base_datos/devoluciones.db')
		self.__cursor2 = self.__con2.cursor()
		
		
		#guardar datos de articulos
		self.btn_guardar_datos.clicked.connect(self.adicionar_articulo)
		
		#realizar venta
		self.btn_vender.clicked.connect(self.adicionar_venta)
		
		# para validar que en el campo cantidad solo se escriban numeros
		validator = QtGui.QDoubleValidator()
		self.cant_articulo.setValidator(validator)
		
		# para validar que en el campo precio costo solo se escriban numeros
		validator = QtGui.QDoubleValidator()
		self.precio_costo.setValidator(validator)
		
		# para validar que en el campo precio venta solo se escriban numeros
		validator = QtGui.QDoubleValidator()
		self.precio_venta.setValidator(validator)
		
		# para validar que en el campo cantidad (en la venta) solo se escriban numeros
		validator = QtGui.QDoubleValidator()
		self.cantidad_vendida.setValidator(validator)
		
		# para validar que en el campo precio (en la venta) solo se escriban numeros
		validator = QtGui.QDoubleValidator()
		self.precio.setValidator(validator)	
		
		# para validar que en el campo pago (en la venta) solo se escriban numeros
		validator = QtGui.QDoubleValidator()
		self.pago_adelantado.setValidator(validator)	
		
		# mando a cargar todos los artuculos insertados
		self.listar_articulos_tabla()
		
		#mando a listar todas las ventas
		self.listar_ventas_tabla()
		
		
		#mando a listar todas las devoluciones
		self.listar_devoluciones_tabla()
		
		# muestro el inventario
		self.inventario()
		
		# muestro en el combobox los articulos registrados
		self.listado_articulos()
		
		
		# saber la fila que ha sido seleccionada (articulo seleccionado)
		self.tabla_relacion_articulo.clicked.connect(self.fila_seleccionada)
		
		# eliminar articulo
		self.btn_eliminar_articulo.clicked.connect(self.eliminar_articulo)
		
		
		# eliminar venta
		self.btn_eliminar_venta.clicked.connect(self.eliminar_venta)		
		
		
		# saber la fila que ha sido seleccionada (venta seleccionado)
		self.tabla_relacion_ventas.clicked.connect(self.fila_seleccionada_venta)
		
		
		# buscar articulos por los fitros
		self.btn_filtar_articulo.clicked.connect(self.buscar_articulo)
		
		
		# buscar ventas por los filtros
		self.btn_filtrar_venta.clicked.connect(self.buscar_venta)
		
		# reporte por cliente
		self.btn_buscar_reporte_cliente.clicked.connect(self.buscar_cliente)
		
		#filtar devoluciones por cliente
		self.btn_buscar_devoluciones.clicked.connect(self.buscar_devoluciones)
		
		
		# opcion para devolver articulos
		self.btn_devolver.clicked.connect(self.devolver_articulo)
		
		# hacer una devolucion
		self.btn_actualizar_devoluciones.clicked.connect(self.hacer_devolucion)
		
		# pagar dinero de un articulo
		self.btn_pagar.clicked.connect(self.pagar_articulo)
		
		# btn actualizar pago de una venta
		self.btn_actualizar.clicked.connect(self.actualizar_pago_venta)
		
		
		#el btn de Actualizar pago sale por defecto invisible
		self.btn_actualizar.setVisible(False)
		
		
		# el btn actualizar_devoluciones sale inicialmente invisible
		self.btn_actualizar_devoluciones.setVisible(False)
		
		
		# el btn pagar estara inhabilidato hasta que se seleccione una fila de la tabla ventas
		self.btn_pagar.setEnabled(False)
		
		# el btn Eliminar articulo estara inhabilidato hasta que se seleccione una fila de la tabla articulos
		self.btn_eliminar_articulo.setEnabled(False)
		
		# el btn Eliminar venta estara inhabilidato hasta que se seleccione una fila de la tabla venta
		self.btn_eliminar_venta.setEnabled(False)
		
		# el btn Devolver estara inhabilitado hasta que se seleccione una fila de la tabla ventas
		self.btn_devolver.setEnabled(False)
		
		# variables
		self.formulario_articulo_valido = None
		self.formulario_ventas_valido = None
		
		# actualizar la caja
		self.actualizar_caja()
		
		
		
		#~ self.articulo_vendido.currentIndexChanged.connect(self.prueba)
#~ 
		#~ 
	#~ def prueba(self):
		#~ print "entroo"
		#~ print self.articulo_vendido.currentText(), "forrillo"
		
	
	def validar_datos_formulario_articulo(self):
		
		# expresion regular para validar la fecha
		fecha = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/(0?[1-9]|[12][0-9]|3[01])$')
		
		#***campo fecha
		if self.fecha_entrada == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Fecha</b> es obligatorio llenarlo")
			self.formulario_articulo_valido = False
			return 	
					
		 
		#~ print self.fecha_entrada, "fecha"
		#~ if fecha.search(str(self.fecha_entrada))==None:
			#~ QMessageBox.information(self, u"Error", u"La fecha es incorrecta. El formato correcto es: <b>DD/MM/AA</b>")
			#~ self.formulario_articulo_valido = False
			#~ return
		
			
		#***campo articulo
		if self.articulo_entrado == "--Seleccione--" or len(self.articulo_entrado) == 0:
			QMessageBox.critical(self, u"Error", u"El campo <b>Articulo</b> es obligatorio llenarlo")
			self.formulario_articulo_valido = False
			return
		else:
			#verificar si el articulo que se desea ingresar ya esta en la lista de articulo
			# si coincide la fecha,el nombre, y el precio de costo
			lista_articulos=self.consulta_articulos()
			
			if self.fecha_entrada and self.articulo_entrado and self.precioCosto:
				art=(self.fecha_entrada,self.articulo_entrado,unicode(self.precioCosto))

				if art in lista_articulos:
					QMessageBox.critical(self, u"Error", u"El articulo " +"<b>"+ self.articulo_entrado +"</b>"+ " ya ha sido registrado para esta fecha y ese mismo precio de costo")
					self.formulario_articulo_valido = False
					return
 
				
		#***campo cantidad de articulo
		if self.cantArticulo == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Cantidad</b> es obligatorio llenarlo")
			self.formulario_articulo_valido = False
			return 
			
		#***campo precio costo
		if self.precioCosto == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Precio costo</b> es obligatorio llenarlo")
			self.formulario_articulo_valido = False
			return 
			
		#***campo precio venta
		if self.precioVenta == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Precio venta</b> es obligatorio llenarlo")
			self.formulario_articulo_valido = False
			return 
			
			
		self.formulario_articulo_valido = True
			
	
	def validar_datos_formulario_venta(self):
		
		# expresion regular para validar las fechas
		fecha = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/(0?[1-9]|[12][0-9]|3[01])$')
		
		if self.fechVenta == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Fecha</b> es obligatorio llenarlo")
			self.formulario_ventas_valido = False
			return
			 			
				
		#~ if fecha.search(str(self.fechVenta))==None:
			#~ QMessageBox.information(self, u"Error", u"La fecha de compra es incorrecta. El formato correcto es: <b>DD/MM/AA</b>")
			#~ self.formulario_articulo_valido = False
			#~ return
			
		if self.comprador == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Cliente</b> es obligatorio llenarlo")
			self.formulario_ventas_valido = False
			return 
			
		if self.articuloVendido == "--Seleccione--":
			QMessageBox.critical(self, u"Error", u"El campo <b>Articulo</b> es obligatorio, debe seleccionar un articulo ")
			self.formulario_ventas_valido = False
			return
		
		if self.cantidadVendida == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Cantidad</b> es obligatorio llenarlo")
			self.formulario_ventas_valido = False
			return
			
		if self.precioVendido == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Precio</b> es obligatorio llenarlo")
			self.formulario_ventas_valido = False
			return
			
		if self.fechaPago == "":
			QMessageBox.critical(self, u"Error", u"El campo <b>Fecha de pago</b> es obligatorio llenarlo")
			self.formulario_ventas_valido = False
			return
			
		
		#~ if fecha.search(str(self.fechaPago))==None:
			#~ QMessageBox.information(self, u"Error", u"La fecha de pago es incorrecta. El formato correcto es: <b>DD/MM/AA</b>")
			#~ self.formulario_articulo_valido = False
			#~ return
			
			
		# verificar si se cuenta con una cantidad disponible de ese articulo
		
			
		self.formulario_ventas_valido = True
		  
			
	def datos_formulario_articulos(self):
		# Obtener los datos del formulario articulo	
		self.fecha_entrada= unicode(self.fecha.text().toUtf8(), encoding = "utf-8")
		self.articulo_entrado= unicode(self.articulo.currentText())
		self.cantArticulo= self.cant_articulo.text()
		self.precioCosto= self.precio_costo.text()
		self.precioVenta= self.precio_venta.text()
		
		
	def datos_formulario_ventas(self):
		# Obtener los datos del formulario ventas
		self.fechVenta= str(unicode(self.fecha_compra.text().toUtf8(), encoding = "utf-8"))
		self.comprador= unicode(self.cliente.text().toUtf8(), encoding = "utf-8")
		#~ self.articuloVendido= unicode(self.articulo_vendido.text().toUtf8(), encoding = "utf-8")
		self.articuloVendido = self.articulo_vendido.currentText()
		self.cantidadVendida= self.cantidad_vendida.text()
		self.precioVendido= self.precio.text()
		self.pagoAdelantado = self.pago_adelantado.text()
		if self.pagoAdelantado == "":
			self.pagoAdelantado = 0.0

			
		self.fechaPago= unicode(self.fecha_pago.text().toUtf8(), encoding = "utf-8")
		
		
	def limpiar_formulario_articulos(self):
		dt = datetime.date.today()
		self.fecha.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
		#~ self.articulo.setText("")
		self.articulo.setCurrentIndex(0)
		self.cant_articulo.setText("")
		self.precio_costo.setText("")
		self.precio_venta.setText("")
        
		
	def limpiar_formulario_ventas(self):
		#~ self.fecha_compra.setText("")
		dt = datetime.date.today()
		self.fecha_compra.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
		self.cliente.setText("")
		#~ self.articulo_vendido.setText("")
		self.articulo_vendido.setCurrentIndex(0)
		
		self.cantidad_vendida.setText("")
		self.precio.setText("")
		self.pago_adelantado.setText("")
		#~ self.fecha_pago.setText("")
		self.fecha_pago.setDate(QtCore.QDate(dt.year, dt.month, dt.day))		
	
		
	def calcular_importe_articulos(self):

		if self.cantArticulo!= "" and self.precioCosto!= "":
			self.importe = float(self.cantArticulo) * float(self.precioCosto)
		else:
			return
		
	def calcular_beneficio_compra(self):

		if  self.cantArticulo!= "" and self.precioVenta!= "":
			self.beneficio = (int(self.cantArticulo) * float(self.precioVenta))- self.importe
		else:
			return
			
	def calcular_total_pagar_cliente(self):
		
		if self.cantidadVendida!= "" and self.precioVendido!= "":
			self.total_a_pagar = float(self.cantidadVendida)* float(self.precioVendido)
		else:
			return
		
		
			
	def listar_articulos_tabla(self):
		articulos = self.consulta_seleccionar_todos_articulos()
		
		self.tabla_relacion_articulo.setRowCount(len(articulos))
		columna=0
		for fila, valor in enumerate(articulos):
			self.tabla_relacion_articulo.setItem(fila, columna, QTableWidgetItem(unicode(valor[1])))
			self.tabla_relacion_articulo.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[2])))
			self.tabla_relacion_articulo.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[3])))
			self.tabla_relacion_articulo.setItem(fila, columna+3, QTableWidgetItem(unicode(valor[4])))
			self.tabla_relacion_articulo.setItem(fila, columna+4, QTableWidgetItem(unicode(valor[5])))
			self.tabla_relacion_articulo.setItem(fila, columna+5, QTableWidgetItem(unicode(valor[6])))
			self.tabla_relacion_articulo.setItem(fila, columna+6, QTableWidgetItem(unicode(valor[7])))
	
	def listar_articulos_tabla_filtro(self, articulos):		
		self.tabla_relacion_articulo.setRowCount(len(articulos))
		columna=0
		for fila, valor in enumerate(articulos):
			self.tabla_relacion_articulo.setItem(fila, columna, QTableWidgetItem(unicode(valor[1])))
			self.tabla_relacion_articulo.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[2])))
			self.tabla_relacion_articulo.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[3])))
			self.tabla_relacion_articulo.setItem(fila, columna+3, QTableWidgetItem(unicode(valor[4])))
			self.tabla_relacion_articulo.setItem(fila, columna+4, QTableWidgetItem(unicode(valor[5])))
			self.tabla_relacion_articulo.setItem(fila, columna+5, QTableWidgetItem(unicode(valor[6])))
			self.tabla_relacion_articulo.setItem(fila, columna+6, QTableWidgetItem(unicode(valor[7])))
	
	def listar_articulos_tabla_inventario(self, articulos):	
		# muestro solo los articulos que tienen existencia, es decir, que su cantidad es mayor a cero
		aunx=[]
		[aunx.append(i) for i in articulos if i[1]>0]
				
		self.tabla_inventario.setRowCount(len(aunx))
		columna=0
		for fila, valor in enumerate(aunx):
			self.tabla_inventario.setItem(fila, columna, QTableWidgetItem(unicode(valor[0])))
			self.tabla_inventario.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[1])))
			self.tabla_inventario.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[2])))
	
			
	def listar_ventas_tabla(self):
		ventas = self.consulta_seleccionar_todas_ventas()
		
		self.tabla_relacion_ventas.setRowCount(len(ventas))
		columna=0
		for fila, valor in enumerate(ventas):
			self.tabla_relacion_ventas.setItem(fila, columna, QTableWidgetItem(unicode(valor[1])))
			self.tabla_relacion_ventas.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[2])))
			self.tabla_relacion_ventas.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[3])))
			self.tabla_relacion_ventas.setItem(fila, columna+3, QTableWidgetItem(unicode(valor[4])))
			self.tabla_relacion_ventas.setItem(fila, columna+4, QTableWidgetItem(unicode(valor[5])))
			self.tabla_relacion_ventas.setItem(fila, columna+5, QTableWidgetItem(unicode(valor[6])))
			self.tabla_relacion_ventas.setItem(fila, columna+6, QTableWidgetItem(unicode(valor[7])))
			self.tabla_relacion_ventas.setItem(fila, columna+7, QTableWidgetItem(unicode(valor[8])))
			self.tabla_relacion_ventas.setItem(fila, columna+8, QTableWidgetItem(unicode(valor[9])))
			self.tabla_relacion_ventas.setItem(fila, columna+9, QTableWidgetItem(unicode(valor[10])))
	
	def listar_devoluciones_tabla(self):
		devoluciones = self.consulta_seleccionar_todas_devoluciones()
		
		self.tabla_reporte_devoluciones.setRowCount(len(devoluciones))
		columna=0
		for fila, valor in enumerate(devoluciones):
			self.tabla_reporte_devoluciones.setItem(fila, columna, QTableWidgetItem(unicode(valor[2])))
			self.tabla_reporte_devoluciones.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[3])))
			self.tabla_reporte_devoluciones.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[4])))
			self.tabla_reporte_devoluciones.setItem(fila, columna+3, QTableWidgetItem(unicode(valor[5])))

	def listar_devoluciones_tabla_filtro(self, devoluciones):
		self.tabla_reporte_devoluciones.setRowCount(len(devoluciones))
		columna=0
		for fila, valor in enumerate(devoluciones):
			self.tabla_reporte_devoluciones.setItem(fila, columna, QTableWidgetItem(unicode(valor[2])))
			self.tabla_reporte_devoluciones.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[3])))
			self.tabla_reporte_devoluciones.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[4])))
			self.tabla_reporte_devoluciones.setItem(fila, columna+3, QTableWidgetItem(unicode(valor[5])))
			
			
			
	def listar_ventas_tabla_filtro(self, ventas):
		self.tabla_relacion_ventas.setRowCount(len(ventas))
		columna=0
		for fila, valor in enumerate(ventas):
			self.tabla_relacion_ventas.setItem(fila, columna, QTableWidgetItem(unicode(valor[1])))
			self.tabla_relacion_ventas.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[2])))
			self.tabla_relacion_ventas.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[3])))
			self.tabla_relacion_ventas.setItem(fila, columna+3, QTableWidgetItem(unicode(valor[4])))
			self.tabla_relacion_ventas.setItem(fila, columna+4, QTableWidgetItem(unicode(valor[5])))
			self.tabla_relacion_ventas.setItem(fila, columna+5, QTableWidgetItem(unicode(valor[6])))
			self.tabla_relacion_ventas.setItem(fila, columna+6, QTableWidgetItem(unicode(valor[7])))
			self.tabla_relacion_ventas.setItem(fila, columna+7, QTableWidgetItem(unicode(valor[8])))
			self.tabla_relacion_ventas.setItem(fila, columna+8, QTableWidgetItem(unicode(valor[9])))
			self.tabla_relacion_ventas.setItem(fila, columna+9, QTableWidgetItem(unicode(valor[10])))
	
		
	def adicionar_articulo(self):		
		# obtengo los datos del formulario
		self.datos_formulario_articulos()
				
		# valido los datos del formulario
		self.validar_datos_formulario_articulo()
		
		if self.formulario_articulo_valido == True:
			#calculo el importe  de la compra por cada articulo
			self.calcular_importe_articulos()
			
			# calculo el beneficio de la compra por cada articulo
			self.calcular_beneficio_compra()		
					
			# mando a insertar el nuevo articulo
			self.consulta_insertar_articulos()
			
			#actualizo la lista de articulos
			self.listar_articulos_tabla()
			
			
			#limpio los campos del formulario
			self.limpiar_formulario_articulos()
					
			# mensaje de confirmacion
			QMessageBox.information(self, u"Información", u"El articulo ha sido agregado correctamente")
			
			#actualizo el inventario
			self.inventario()
			
			#actualizar la caja
			self.actualizar_caja()
			
			
			# actualizar listado de articulos en el combox de la venta
			self.listado_articulos()

		
	def adicionar_venta(self):
		# obtengo los datos del formulario
		self.datos_formulario_ventas()
		
		#valido los datos del formulario
		self.validar_datos_formulario_venta()
		
		if self.formulario_ventas_valido == True:
			#calculo el total a pagar por el cliente
			self.calcular_total_pagar_cliente()
					
			#mando a insertar la nueva venta
			self.consulta_insertar_venta()
			
			#actualizo la lista de ventas
			self.listar_ventas_tabla()
			
			#limpio los campos del formulario
			self.limpiar_formulario_ventas()
			
			# mensaje de confirmacion
			QMessageBox.information(self, u"Información", u"Se ha realizado la venta correctamente")

		
		#actualizo el inventario
		self.inventario()
			
		#actualizar la caja
		self.actualizar_caja()

	def buscar_articulo(self):
		#Funcion para buscar las articulos segun los filtros
		
		#obtengo los datos del formulario
		fecha= unicode(self.filtro_fecha_compra.text().toUtf8(), encoding = "utf-8")
		articulo= unicode(self.filtro_articulo_comprado.text().toUtf8(), encoding = "utf-8")
		precio_venta = str(self.filtro_precio_venta.text())
		
		datos=[fecha, articulo, precio_venta]
		#mando a hacer la consulta con los datos registrados por el usuario
		filtrados=self.consulta_filtrar_articulos(datos)
		
		if len(filtrados)==0:
			QMessageBox.information(self, u"Información", u"No se encontraron articulos con esos datos")
			return
		if len(filtrados)>0:
			self.listar_articulos_tabla_filtro(filtrados)
		
	def buscar_venta(self):
		#función para buscar las ventas segun los filtros
		
		#obtengo los datos del formulario
		deben=False
		if self.deben.isChecked():
			deben=True
			
			
		articulo= unicode(self.filtro_articulo_vendido.text().toUtf8(), encoding = "utf-8")
		cliente= unicode(self.filtro_cliente_venta.text().toUtf8(), encoding = "utf-8")
		fecha= str(unicode(self.filtro_fecha_pago.text().toUtf8(), encoding = "utf-8"))
		
		datos=[articulo, cliente, deben, fecha]
		
		#mando a hacer la consulta con los datos registrados por el usuario
		filtradas= self.consulta_filtrar_ventas(datos)
		
		if len(filtradas)==0:
			QMessageBox.information(self, u"Información", u"No se encontraron ventas con esos datos")
			return
			
		if len(filtradas)>0:
			self.listar_ventas_tabla_filtro(filtradas)

		
	
	def fila_seleccionada(self):

		#retorna la fila seleccionada
		
		# se activa el btn Eliminar para poder eliminar un articulo
		self.btn_eliminar_articulo.setEnabled(True)
	
		# obtengo el numero de la fila seleccionada
		self.tabla_relacion_articulo.currentRow()
		# obtener el texto de la fila seleccionada
		fil_seleccionada = self.tabla_relacion_articulo.selectedItems()	

		#guardo en una lista el contenido de la fila
		self.contenido_fila=[]
		for celda in fil_seleccionada:
			self.contenido_fila.append(celda.text())
			
		# mando a hacer la consulta con todos los datos de la fila seleccionada (articulo seleccionado)
		datos= self.consulta_buscar_fila_seleccionada(self.contenido_fila)
			
		return self.tabla_relacion_articulo.currentRow(), self.contenido_fila

	def fila_seleccionada_venta(self):

		#retorna la fila seleccionada
		
		# se activa el btn para poder pagar una deuda
		self.btn_pagar.setEnabled(True)
		# se activa el btn para poder eliminar una venta
		self.btn_eliminar_venta.setEnabled(True)
		# se activa el btn para poder devolver articulos de una venta
		self.btn_devolver.setEnabled(True)
		
	
		# obtengo el numero de la fila seleccionada
		self.tabla_relacion_ventas.currentRow()
		# obtener el texto de la fila seleccionada
		fil_seleccionada = self.tabla_relacion_ventas.selectedItems()	

		#guardo en una lista el contenido de la fila
		self.contenido_fila_venta=[]
		for celda in fil_seleccionada:
			self.contenido_fila_venta.append(celda.text())
			
			
		# mando a hacer la consulta con todos los datos de la fila seleccionada (venta seleccionado)
		datos= self.consulta_buscar_fila_seleccionada_ventas(self.contenido_fila_venta)
			
		return self.tabla_relacion_ventas.currentRow(), self.contenido_fila_venta

	
	
	def pagar_articulo(self):
		
		cliente = self.fila_seleccionada_venta()[1]
		
		#activo la pestaña correspondiente
		self.tabWidget.setCurrentIndex(2)
		# pongo visible el btn de actualizar el pago
		self.btn_actualizar.setVisible(True)
		
		# inhabilito el btn vender
		self.btn_vender.setEnabled(False)		
		
		#relleno los campos del cliente correspondiente
		fecha= cliente[0].split("/")
		# como la fecha es inferior al mínimo, los widgets muestran el texto de valor especial (en este caso la fecha que le paso por parametro )
		self.fecha_compra.setDate(QDate.fromString( "01/01/0001", "dd/MM/yyyy"))
		self.fecha_compra.setSpecialValueText( str(fecha[0])+"/"+str(fecha[1])+"/"+str(fecha[2]))
		self.fecha_compra.setEnabled(False)
		
		
		self.cliente.setText(cliente[1])
		self.cliente.setEnabled(False)
		
		# muestro el articulo correspondiente
		AllItems = [self.articulo_vendido.itemText(i) for i in range(self.articulo_vendido.count())]
		# si el articulo ya habia sido eliminado de la lista de articulos
		if not cliente[2] in AllItems:
			self.articulo_vendido.setEnabled(False)
			QMessageBox.information(self, u"Información", u"Ese articulo fue eliminado pero puede efectuar el pago de todas formas")			
		else:	
			self.articulo_vendido.setCurrentIndex(AllItems.index(cliente[2]))
			self.articulo_vendido.setEnabled(False)
		
		# muestro la cntidad vendida
		self.cantidad_vendida.setText(cliente[3])
		self.cantidad_vendida.setEnabled(False)
		
		# muestro el precio
		self.precio.setText(cliente[4])
		self.precio.setEnabled(False)
		
		#Muestro la fecha de pago
		fecha= cliente[-2].split("/")
		self.fecha_pago.setDate(QDate.fromString( "01/01/0001", "dd/MM/yyyy"))
		self.fecha_pago.setSpecialValueText( str(fecha[0])+"/"+str(fecha[1])+"/"+str(fecha[2]))
		self.fecha_pago.setEnabled(False)
		
	def inicializar_formulario_ventas(self):
		# pongo visible el btn de actualizar el pago
		self.btn_actualizar.setVisible(False)
		
		# inhabilito el btn vender
		self.btn_vender.setEnabled(True)
		#habilito los campus
		self.fecha_compra.setEnabled(True)
		self.cliente.setEnabled(True)
		self.articulo_vendido.setEnabled(True)
		self.cantidad_vendida.setEnabled(True)
		self.precio.setEnabled(True)
		self.fecha_pago.setEnabled(True)
		self.pago_adelantado.setEnabled(True)
		
		
		#limpio los campus del formulario ventas
		self.limpiar_formulario_ventas()		
		
			
		
	def actualizar_pago_venta(self):
		# mando a hacer la consulta con todos los datos de la fila seleccionada (venta seleccionado)		
		cliente = self.fila_seleccionada_venta()[1]
		datos=[]
		for c in cliente:
			datos.append(c)
		#obtengo el id de la venta que se desea pagar
		id_venta_a_pagar= self.consulta_buscar_fila_seleccionada_ventas_id(datos)[0][0]	
		
		# obtengo el valor que esta en el campo para pagar
		cantidad_a_pagar = self.pago_adelantado.text()
		if cantidad_a_pagar!="":
			#hago la consulta para actualizar lo que pago y lo que queda debiendo
			self.consulta_actualizar_venta(id_venta_a_pagar, cantidad_a_pagar, datos)
			#mando a listar todas las ventas
			self.listar_ventas_tabla()
			#activo la pestaña correspondiente
			self.tabWidget.setCurrentIndex(3)
			#inicializo todo el formulario de realizar las ventas
			self.inicializar_formulario_ventas()
			
			#actualizo el inventario
			self.inventario()
			
			#actualizar la caja
			self.actualizar_caja()
			
		else:
			QMessageBox.information(self, u"Información", u"No se actualizará la deuda del cliente porque no se introdujo un pago")
			#activo la pestaña correspondiente
			self.tabWidget.setCurrentIndex(3)
			#inicializo todo el formulario de realizar las ventas
			self.inicializar_formulario_ventas()
			
		
		
	def eliminar_articulo(self):
		
		# fila del articulo
		fila = self.fila_seleccionada()[0]
		
		resp = QMessageBox.question(self, u'Pregunta', u'¿Esta seguro que desea <b>eliminar</b> el articulo seleccionado?',
			   QMessageBox.Yes | QMessageBox.No)
		if resp == QMessageBox.Yes:	
			# elimino de la base de datos el articulo
			self.consulta_eliminar_articulo()			
			# elimino en lo visual
			self.tabla_relacion_articulo.removeRow(fila)
		else:
			return
			
		#actualizo el inventario
		self.inventario()
		
		#actualizar la caja
		self.actualizar_caja()
		
		# actualizar listado de articulos en el combox de la venta
		self.listado_articulos()
		
			
	def eliminar_venta(self):
		
		# fila del articulo
		fila = self.fila_seleccionada_venta()[0]		
		
		resp = QMessageBox.question(self, u'Pregunta', u'¿Esta seguro que desea <b>eliminar</b> la venta seleccionada?',
			   QMessageBox.Yes | QMessageBox.No)
		if resp == QMessageBox.Yes:	
			# elimino de la base de datos la venta
			self.consulta_eliminar_venta()			
			# elimino en lo visual
			self.tabla_relacion_ventas.removeRow(fila)
			
			#actualizo el inventario
			self.inventario()
						
			#actualizar la caja
			self.actualizar_caja()
				
		else:
			return
			

			
	def inventario(self):
		#selecciono todos los articulos con su cantidad
		articulos = self.consulta_seleccionar_articulo_cantidad()
		
		#selecciono todas las ventas con su cantidad
		ventas = self.consulta_seleccionar_ventas_cantidad()
		
		# si no se han realizado ventas muestro todos los articulos en el inventario
		if len(ventas)==0:
			self.listar_articulos_tabla_inventario(articulos)
			
		else:		
			quedan=[]
			lista_aux_venta=[]
			
			# para unificar las ventas
			dict={}
			for venta in ventas:
				if venta[0] in dict:
					dict[venta[0]] = dict[venta[0]] + venta[1]		
				else:
					dict[venta[0]] = venta[1]
			# para convertir el diccionario a lista de tuplas:
			lista_aux_venta= dict.items()
			
			# descontar de la cantidad de articulos los que se han vendido	
			for articulo in articulos:
				for pos,venta in enumerate(lista_aux_venta):
					if articulo[0]==venta[0]:
						quedan.append((articulo[0],articulo[1]-venta[1], articulo[2]))
						break
					if articulo[0]!=venta[0] and pos == len(lista_aux_venta)-1:
						quedan.append(articulo)
						
			#listo el inventario en la tabla
			self.listar_articulos_tabla_inventario(quedan)
	
	
	def actualizar_caja(self):
		#calcular beneficio de los articulos
		self.beneficio1 = self.consulta_calcular_beneficio()
		if self.beneficio1 == None:
			self.estimado.setText("0.0")
			self.estimado.setReadOnly(True)			
		else:
			self.estimado.setText(str(self.beneficio1))
			self.estimado.setReadOnly(True)
		
		#calcular inversion de los articulos
		self.inversion1 = self.consulta_calcular_inversion()
		if self.inversion1 == None:
			self.inversion.setText("0.0")
			self.inversion.setReadOnly(True)
		else:
			self.inversion.setText(str(self.inversion1))
			self.inversion.setReadOnly(True)
		
		#calcular deudas de las ventas
		self.deud= self.consulta_calcular_deudas()
		if self.deud == None:
			self.deudas.setText("0.0")
			self.deudas.setReadOnly(True)
		else:
			self.deudas.setText(str(self.deud))
			self.deudas.setReadOnly(True)		
		
		#calcular lo recaudado de las ventas
		self.recaud=self.consulta_calcular_recaudado()
		if self.recaud == None:
			self.recaudado.setText("0.0")
			self.recaudado.setReadOnly(True)
		else:
			self.recaudado.setText(str(self.recaud))
			self.recaudado.setReadOnly(True)
		
		#calcular patrimonio de las ventas
		#~ importe = self.consulta_calcular_importe()
		#~ pago_deudas = self.consulta_calcular_pago_mas_deudas()
		patrimonio= self.consulta_calcular_patrimonio()
		if patrimonio == None:
			self.patrimonio.setText("0.0")
			self.patrimonio.setReadOnly(True)	
		else:
			self.patrimonio.setText(str(patrimonio))
			self.patrimonio.setReadOnly(True)
	

	def listado_articulos(self):
		articulos= self.consulta_seleccionar_todos_articulos()
		
		self.articulo_vendido.clear()
		self.articulo.clear()
		
		self.articulo.setEditable(True)
		
		self.articulo_vendido.addItem("--Seleccione--")
		self.articulo.addItem("--Seleccione--")
		
		for articulo in articulos:
			self.articulo_vendido.addItem(unicode(articulo[2]))
			self.articulo.addItem(unicode(articulo[2]))
			

	def buscar_cliente(self):
		cliente= unicode(self.reporte_cliente.text().toUtf8(), encoding = "utf-8")
		if cliente=="":
			QMessageBox.information(self, u"Información", u"Para mostrar un reporte debe escribir el nombre de un cliente")
			self.tabla_reporte_cliente.clearContents()
			return			
		else:
			datos= self.consulta_filtrar_ventas_cliente(cliente)
			if len(datos)==0:
				QMessageBox.information(self, u"Información", u"Usted no ha realizado ventas a: " +"<b>"+ cliente+"</b>" +u". Revise que el nombre esté correctamente escrito" )
				return

		self.tabla_reporte_cliente.clearContents()
		
		self.tabla_reporte_cliente.setRowCount(len(datos))
		
		columna=0
		total=0
		final=0
		for fila, valor in enumerate(datos):
			self.tabla_reporte_cliente.setItem(fila, columna, QTableWidgetItem(unicode(valor[0])))
			self.tabla_reporte_cliente.setItem(fila, columna+1, QTableWidgetItem(unicode(valor[1])))
			self.tabla_reporte_cliente.setItem(fila, columna+2, QTableWidgetItem(unicode(valor[2])))
			total+=float(valor[2])
			if fila == len(datos)-1:
				item1 = QtGui.QTableWidgetItem(str(total))				
				item1.setBackground(QtGui.QColor("red"))
				font = QFont()
				font.setBold(True)	
				item1.setFont(font)	
				self.tabla_reporte_cliente.setItem(fila, columna+3, (item1))

	
	
	def devolver_articulo(self):
		venta = self.fila_seleccionada_venta()[1]
		
		# obtener el id de la venta seleccionada
		
		
		#activo la pestaña correspondiente
		self.tabWidget.setCurrentIndex(2)
		# pongo visible el btn de actualizar el pago
		self.btn_actualizar_devoluciones.setVisible(True)
		
		# inhabilito el btn vender
		self.btn_vender.setEnabled(False)		
		self.btn_actualizar.setEnabled(False)		
		
		
		#relleno los campos del cliente correspondiente
		fecha= venta[0].split("/")
		# como la fecha es inferior al mínimo, los widgets muestran el texto de valor especial (en este caso la fecha que le paso por parametro )
		self.fecha_compra.setDate(QDate.fromString( "01/01/0001", "dd/MM/yyyy"))
		self.fecha_compra.setSpecialValueText( str(fecha[0])+"/"+str(fecha[1])+"/"+str(fecha[2]))
		self.fecha_compra.setEnabled(False)
		
		
		self.cliente.setText(venta[1])
		self.cliente.setEnabled(False)
		
		# muestro el articulo correspondiente
		AllItems = [self.articulo_vendido.itemText(i) for i in range(self.articulo_vendido.count())]
		self.articulo_vendido.setCurrentIndex(AllItems.index(venta[2]))
		self.articulo_vendido.setEnabled(False)
		
		# inhabilito la opcion para entrar el pago adelantado
		self.pago_adelantado.setEnabled(False)
		
		
		#Muestro la fecha de pago que tenia esa venta y que ahora puede cambiar
		fecha= venta[-2].split("/")
		self.fecha_pago.setDate(QDate.fromString( "01/01/0001", "dd/MM/yyyy"))
		self.fecha_pago.setSpecialValueText( str(fecha[0])+"/"+str(fecha[1])+"/"+str(fecha[2]))
		
		return venta

		
		
	def hacer_devolucion(self):
		
		#obtener los datos del formulario
		fechaPago= unicode(self.fecha_pago.text().toUtf8(), encoding = "utf-8")
		cantidad_devuelta= self.cantidad_vendida.text()
		precio= self.precio.text()
		
		# cuando presiona el btn actualizar sin llenar el campo cantidad y precio
		if cantidad_devuelta=="" and precio =="":
			QMessageBox.information(self, u"Información", u"Para realizar una devolución es necesario llenar el campo cantidad, por tanto no se realizará ninguna devolución")
			self.inicializar_formulario_ventas()
			self.btn_actualizar_devoluciones.setVisible(False)
			self.tabWidget.setCurrentIndex(3)
			return
		
		# si lleno el campo precio y no lleno el campo cantidad
		if cantidad_devuelta=="" and precio !="":
			QMessageBox.critical(self, u"Error", u"Para hacer una devolución el campo <b>Cantidad</b> es obligatorio llenarlo")
			return
			
		# obtener el id de la venta que se quiere actualizar
		id_venta_actualizar=self.consulta_obtener_id_venta(self.devolver_articulo())
		
		# ********insertar la devolucion en la tabla devoluciones**********
		fecha_hoy = datetime.date.today().strftime("%d/%m/%Y")
		cliente = self.devolver_articulo()[1]
		articulo = self.devolver_articulo()[2]
		
		
		# cantidad anterior que tenia del articulo
		cantidad_anterior= self.devolver_articulo()[3]
		# calculo la cantidad que le queda ahora
		cantidad_resultante= int(cantidad_anterior)-int(cantidad_devuelta)
		
		# calculo la nueva cantidad a pagar a partir de la nueva cantidad de articulos
		if precio!= "":
			total_a_pagar = float(cantidad_resultante)* float(precio)
		else:
			# si no se especifico un nuevo precio la cantidad a pagar se calcula con el precio antiguo que tenia la venta
			total_a_pagar = float(cantidad_resultante)* float(self.devolver_articulo()[4])
			
		# Al devolver articulos es necesario recalcular la deuda
		deuda= total_a_pagar-float(self.devolver_articulo()[6])
		
				
				
		# no puede devolver una cantidad mayor a la que tenia
		if cantidad_anterior<cantidad_devuelta:
			QMessageBox.critical(self, u"Error", u"No puede devolver una cantidad mayor a la que tenía")
			return
			
		# si esta devolviendo todos los articulos
		if cantidad_resultante == 0:
			resp = QMessageBox.question(self, u'Pregunta', u'Esta devolviendo todos los articulos que había comprado. Esto provoca que se elimine la venta, ¿Esta seguro que desea continuar?', QMessageBox.Yes | QMessageBox.No)
					   
			if resp == QMessageBox.Yes:	
				# elimino de la base de datos el articulo
				self.consulta_eliminar_venta_por_id(id_venta_actualizar)
				QMessageBox.information(self, u"Información", u"La venta ha sido eliminada")
				# actualizo la tabla de ventas
				self.listar_ventas_tabla()
				#muestro la pestaña del listado de las ventas
				self.tabWidget.setCurrentIndex(3)
				#inicializo el formulario de las ventas
				self.inicializar_formulario_ventas()
				#actualizo la caja
				self.actualizar_caja()
				# actualizo el inventario
				self.inventario()
				
			else:
				return
		
		# inserto la devolucion
		datos=[id_venta_actualizar, fecha_hoy, cliente, articulo, cantidad_devuelta]
		self.consulta_insertar_devolucion(datos)
		QMessageBox.information(self, u"Información", u"Se ha realizado la devolución correctamente")
		
		# actualizo lo venta que ha sido modificada
		# se actualizan tambien los campos cantidad, precio, totalpagar,debe,fechapago y el campo devolvio que se pone en SI		
		datos_venta=[cantidad_resultante, precio, total_a_pagar, deuda, fechaPago, "Si" ]		
		self.consulta_actualizar_venta_por_devolucion(id_venta_actualizar, datos_venta)
		self.inicializar_formulario_ventas()
		self.listar_ventas_tabla()
		self.listar_devoluciones_tabla()
		#actualizo la caja
		self.actualizar_caja()
		# actualizo el inventario
		self.inventario()
		self.btn_actualizar_devoluciones.setVisible(False)
		self.tabWidget.setCurrentIndex(3)	
		
	
		
	def buscar_devoluciones(self):
		cliente = unicode(self.reporte_devoluciones.text().toUtf8(), encoding = "utf-8")
		
		if len(cliente)==0:
			devoluciones = self.consulta_seleccionar_todas_devoluciones()
			self.listar_devoluciones_tabla()
		else:
			devoluciones = self.consulta_filtrar_devoluciones_cliente(cliente)
			if len(devoluciones)==0:
				QMessageBox.information(self, u"Información", u"El cliente <b>"+ cliente+ u"</b> no ha efectuado ninguna devolución.")
				return
			else:
				self.listar_devoluciones_tabla_filtro(devoluciones)
		
	
	#***************Interaccion con la BD****************************	
	
	def consulta_insertar_articulos(self):
		if self.fecha_entrada!="" and self.articulo_entrado !="" and self.cantArticulo !="" and self.precioCosto !="" and self.importe !="" and self.precioVenta !="" and self.beneficio!="":
			self.__cursor.execute('insert into articulos (fecha, articulo, cantidad, preciocosto, importe, precioventa, beneficio) values(?,?,?,?,?,?,?);', ((self.fecha_entrada), (self.articulo_entrado), (str(self.cantArticulo)), (str(self.precioCosto)), (str(self.importe)), (str(self.precioVenta)), (str(self.beneficio))))
			self.__con.commit()
		else:   
			return
					

	def consulta_insertar_venta(self):
		self.deuda = float(self.total_a_pagar)-float(self.pagoAdelantado)
		self.__cursor1.execute('insert into ventas (fechacompra, cliente, articulo, cantidad, precio, totalpagar, pago, debe, fechapago, devolvio) values(?,?,?,?,?,?,?,?,?,?);', ((self.fechVenta), (self.comprador), (str(self.articuloVendido)), (str(self.cantidadVendida)), (str(self.precioVendido)), (str(self.total_a_pagar)), (str(self.pagoAdelantado)), (str(self.deuda)), (self.fechaPago), ("No")))
		self.__con1.commit()

		
	def consulta_seleccionar_todos_articulos(self):
		consulta = self.__cursor.execute("select * FROM articulos")
		lista = consulta.fetchall()
		return lista
		
	def consulta_seleccionar_articulo_cantidad(self):
		consulta = self.__cursor.execute("select articulo,cantidad, preciocosto FROM articulos")
		lista = consulta.fetchall()
		return lista
		
		
	def consulta_seleccionar_todas_ventas(self):
		consulta = self.__cursor1.execute("select * FROM ventas")
		lista = consulta.fetchall()
		return lista
		
	def consulta_seleccionar_todas_devoluciones(self):
		consulta = self.__cursor2.execute("select * FROM devoluciones")
		lista = consulta.fetchall()
		return lista		
		
		
	def consulta_seleccionar_ventas_cantidad(self):
		consulta = self.__cursor1.execute("select articulo, cantidad FROM ventas")
		lista = consulta.fetchall()
		return lista
		
			
	def consulta_buscar_fila_seleccionada(self, datos):
		consulta = self.__cursor.execute("select * FROM articulos WHERE fecha='%s' and articulo='%s' and cantidad='%s' and preciocosto='%s' and importe='%s' and precioventa='%s' and beneficio='%s'" % ((unicode(self.contenido_fila[0]), unicode(self.contenido_fila[1]), self.contenido_fila[2], self.contenido_fila[3], self.contenido_fila[4], self.contenido_fila[5], self.contenido_fila[6])))
		lista = consulta.fetchall()
		return lista
		
	def consulta_buscar_fila_seleccionada_ventas(self, datos):
		consulta = self.__cursor1.execute("select * FROM ventas WHERE fechacompra='%s' and cliente='%s' and articulo='%s' and cantidad='%s' and precio='%s' and totalpagar='%s' and fechapago='%s'" % ((unicode(self.contenido_fila_venta[0]), unicode(self.contenido_fila_venta[1]), self.contenido_fila_venta[2], self.contenido_fila_venta[3], self.contenido_fila_venta[4], self.contenido_fila_venta[5], self.contenido_fila_venta[6])))
		lista = consulta.fetchall()
		return lista
		
		
	def consulta_buscar_fila_seleccionada_ventas_id(self, datos):
		consulta = self.__cursor1.execute("select id FROM ventas WHERE fechacompra='%s' and cliente='%s' and articulo='%s' and cantidad='%s' and precio='%s' and totalpagar='%s' and pago='%s' and debe='%s' and fechapago='%s'" % ((unicode(datos[0]), unicode(datos[1]), datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8])))
		lista = consulta.fetchall()
		return lista
		
		
	def consulta_eliminar_articulo(self):
		self.__cursor.execute("DELETE FROM articulos WHERE fecha='%s' and articulo='%s' and cantidad='%s' and preciocosto='%s' and importe='%s' and precioventa='%s' and beneficio='%s'" % ((unicode(self.contenido_fila[0]), unicode(self.contenido_fila[1]), self.contenido_fila[2], self.contenido_fila[3], self.contenido_fila[4], self.contenido_fila[5], self.contenido_fila[6])))
		self.__con.commit()
		
		
	def consulta_eliminar_venta(self):
		self.__cursor1.execute("DELETE FROM ventas WHERE fechacompra='%s' and cliente='%s' and articulo='%s' and cantidad='%s' and precio='%s' and totalpagar='%s' and pago='%s' and debe='%s' and fechapago='%s'" % ((unicode(self.contenido_fila_venta[0]), unicode(self.contenido_fila_venta[1]), self.contenido_fila_venta[2], self.contenido_fila_venta[3], self.contenido_fila_venta[4], self.contenido_fila_venta[5], self.contenido_fila_venta[6], self.contenido_fila_venta[7], self.contenido_fila_venta[8])))
		self.__con1.commit()
		
	def consulta_eliminar_venta_por_id(self, id_venta):
		self.__cursor1.execute("DELETE FROM ventas WHERE id='%s' " % ((id_venta)))
		self.__con1.commit()
		
		
	def consulta_articulos(self):
		consulta = self.__cursor.execute("select fecha, articulo, preciocosto FROM articulos")
		lista = consulta.fetchall()
		return lista
		
	def consulta_calcular_beneficio(self):
		consulta = self.__cursor.execute("select Sum(beneficio) AS Total FROM articulos")
		beneficio = consulta.fetchone()[0]
		return beneficio
		
	def consulta_calcular_inversion(self):
		consulta = self.__cursor.execute("select Sum(preciocosto) AS Total FROM articulos")
		inversion = consulta.fetchone()[0]
		return inversion
		
	def consulta_calcular_recaudado(self):
		consulta = self.__cursor1.execute("select Sum(pago) AS Total FROM ventas")
		recaudado = consulta.fetchone()[0]
		return recaudado
		
	def consulta_calcular_deudas(self):
		consulta = self.__cursor1.execute("select Sum(debe) AS Total FROM ventas")
		deudas = consulta.fetchone()[0]
		return deudas
		
	def consulta_calcular_patrimonio(self):
		consulta = self.__cursor.execute("select Sum((cantidad*precioventa)) AS Total FROM articulos")
		patrimonio = consulta.fetchone()[0]
		return patrimonio
		
	def consulta_calcular_pago_mas_deudas(self):
		consulta = self.__cursor1.execute("select Sum(pago+debe) AS Total FROM ventas")
		recaudado = consulta.fetchone()[0]
		return recaudado
		
	
	
	def consulta_filtrar_articulos(self, datos):
		# si no viene fecha la consulta se hace sin tener en cuenta la fecha
		if datos[0]== " ":
			consulta = self.__cursor.execute("select * FROM articulos WHERE articulo like ? and precioventa like ?  ", (('%'+datos[1]+'%'), ('%'+datos[2]+'%')))
			lista = consulta.fetchall()
		else:
			consulta = self.__cursor.execute("select * FROM articulos WHERE fecha like ? and articulo like ? and precioventa like ?  ", (('%'+datos[0]+'%'), ('%'+datos[1]+'%'), ('%'+datos[2]+'%')))
			lista = consulta.fetchall()
						
		return lista
		
	def consulta_filtrar_ventas(self, datos):
		# si no viene fecha de pago las consultas se hacen sin tener en cuenta la fecha de pago
		if datos[3]== " ":
			if datos[2]==True:
				# consulta con los que deben más de 0.0, es decir, los que deben algo
				consulta = self.__cursor1.execute("select * FROM ventas WHERE articulo like ? and cliente like ? and debe <> '0.0'  ", (('%'+datos[0]+'%'), ('%'+datos[1]+'%')))
			else:
				# consulta con los que no deben 
				consulta = self.__cursor1.execute("select * FROM ventas WHERE articulo like ? and cliente like ?   ", (('%'+datos[0]+'%'), ('%'+datos[1]+'%')))
			lista = consulta.fetchall()			
		
		else:
			if datos[2]==True:
				# consulta con los que deben más de 0.0, es decir, los que deben algo
				consulta = self.__cursor1.execute("select * FROM ventas WHERE articulo like ? and cliente like ? and debe <> '0.0' and fechapago like ?  ", (('%'+datos[0]+'%'), ('%'+datos[1]+'%') , ('%'+datos[3]+'%')))
			else:
				# consulta con los que no deben 
				consulta = self.__cursor1.execute("select * FROM ventas WHERE articulo like ? and cliente like ? and fechapago like ?  ", (('%'+datos[0]+'%'), ('%'+datos[1]+'%') , ('%'+datos[3]+'%')))
			lista = consulta.fetchall()
		
		return lista
		
	def consulta_filtrar_ventas_cliente(self, cliente):
		consulta = self.__cursor1.execute("select fechacompra, articulo, debe FROM ventas WHERE cliente='%s' " % (unicode(cliente)))
		lista = consulta.fetchall()
		return lista
		
		
			
	def consulta_actualizar_venta(self, id_venta, cantidad_pagar,datos):
		datos[6]=float(datos[6])+float(cantidad_pagar)
		debe= float(datos[5])-datos[6]
		
		self.__cursor1.execute('UPDATE ventas SET fechacompra = ?, cliente = ?, articulo = ?, cantidad = ?, precio = ?, totalpagar = ?, pago = ?, debe = ?, fechapago =? WHERE id = ?', ((str(datos[0])), (unicode(datos[1])), (str(datos[2])), (str(datos[3])), (str(datos[4])), (str(datos[5])), (str(datos[6])), (str(debe)), (str(datos[8])), (str(id_venta))))
		self.__con1.commit()
		
	def consulta_obtener_id_venta(self, datos):
		consulta = self.__cursor1.execute("select id FROM ventas WHERE fechacompra='%s' and cliente='%s' and articulo='%s' and cantidad='%s' and precio='%s' and totalpagar='%s' and pago='%s' and debe='%s' and fechapago='%s' and devolvio='%s' " % (unicode(datos[0]), unicode(datos[1]), str(datos[2]), str(datos[3]), str(datos[4]), str(datos[5]), str(datos[6]), str(datos[7]), str(datos[8]), str(datos[9])))
		identificador = consulta.fetchone()
		return identificador[0]
		
	def consulta_insertar_devolucion(self, datos):
		self.__cursor2.execute('insert into devoluciones (idventa, fecha, cliente, articulo, cantidad) values(?,?,?,?,?);', ((int(datos[0])), (str(datos[1])), (str(datos[2])), (str(datos[3])), (int(datos[4]))))
		self.__con2.commit()
		
	def consulta_actualizar_venta_por_devolucion(self, id_venta, datos):
	# datos=[cantidad_resultante, precio, total_a_pagar, deuda, fechaPago, "Si" ]
		#si modifico el precio	
		if datos[1]!="":
			self.__cursor1.execute('UPDATE ventas SET cantidad = ?, precio = ?, totalpagar = ?, debe = ?, fechapago =?, devolvio =? WHERE id = ?', ((int(datos[0])), (str(datos[1])), (str(datos[2])), (str(datos[3])), (str(datos[4])), (str(datos[5])), (id_venta)))
		else:
			self.__cursor1.execute('UPDATE ventas SET cantidad = ?, totalpagar = ?, debe = ?, fechapago =?, devolvio =? WHERE id = ?', ((int(datos[0])), (str(datos[2])), (str(datos[3])), (str(datos[4])), (str(datos[5])), (id_venta)))
		self.__con1.commit()
		
	def consulta_filtrar_devoluciones_cliente(self, cliente):
		consulta = self.__cursor2.execute("select * FROM devoluciones WHERE cliente='%s' " % (unicode(cliente)))
		lista = consulta.fetchall()
		return lista
		#~ if cliente =="Todas":
			#~ print True
			#~ consulta = self.__cursor2.execute("select * FROM devoluciones")
			#~ lista = consulta.fetchall()		
		#~ else:	
			#~ consulta = self.__cursor2.execute("select * FROM devoluciones WHERE cliente='%s' " % (unicode(cliente)))
		#~ lista = consulta.fetchall()
		#~ return lista
'''
	
