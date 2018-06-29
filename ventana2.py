# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana2.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(517, 472)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayoutWidget = QtGui.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 100, 461, 79))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.usuarioLabel = QtGui.QLabel(self.formLayoutWidget)
        self.usuarioLabel.setObjectName(_fromUtf8("usuarioLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.usuarioLabel)
        self.usuario = QtGui.QLineEdit(self.formLayoutWidget)
        self.usuario.setObjectName(_fromUtf8("usuario"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.usuario)
        self.clavePublicaLabel = QtGui.QLabel(self.formLayoutWidget)
        self.clavePublicaLabel.setObjectName(_fromUtf8("clavePublicaLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.clavePublicaLabel)
        self.clave = QtGui.QLineEdit(self.formLayoutWidget)
        self.clave.setObjectName(_fromUtf8("clave"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.clave)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.enviar = QtGui.QPushButton(self.formLayoutWidget)
        self.enviar.setObjectName(_fromUtf8("enviar"))
        self.horizontalLayout.addWidget(self.enviar)
        self.borrar = QtGui.QPushButton(self.formLayoutWidget)
        self.borrar.setObjectName(_fromUtf8("borrar"))
        self.horizontalLayout.addWidget(self.borrar)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(80, 80, 381, 141))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.usuarioLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.usuarioLabel_2.setObjectName(_fromUtf8("usuarioLabel_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.usuarioLabel_2)
        self.usuario2 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.usuario2.setObjectName(_fromUtf8("usuario2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.usuario2)
        self.guardar = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.guardar.setObjectName(_fromUtf8("guardar"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.guardar)
        self.encriptar = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.encriptar.setObjectName(_fromUtf8("encriptar"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.encriptar)
        self.enviar2 = QtGui.QPushButton(self.formLayoutWidget_2)
        self.enviar2.setObjectName(_fromUtf8("enviar2"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.enviar2)
        self.archivoLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.archivoLabel.setObjectName(_fromUtf8("archivoLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.archivoLabel)
        self.archivo = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.archivo.setObjectName(_fromUtf8("archivo"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.archivo)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 517, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.borrar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.usuario.clear)
        QtCore.QObject.connect(self.borrar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clave.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.usuarioLabel.setText(_translate("MainWindow", "Usuario:", None))
        self.clavePublicaLabel.setText(_translate("MainWindow", "Clave publica:", None))
        self.enviar.setText(_translate("MainWindow", "Enviar", None))
        self.borrar.setText(_translate("MainWindow", "Borrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Alta", None))
        self.usuarioLabel_2.setText(_translate("MainWindow", "Usuario:", None))
        self.guardar.setText(_translate("MainWindow", "Guardar", None))
        self.encriptar.setText(_translate("MainWindow", "Encriptar", None))
        self.enviar2.setText(_translate("MainWindow", "enviar", None))
        self.archivoLabel.setText(_translate("MainWindow", "Archivo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Autentificar", None))

