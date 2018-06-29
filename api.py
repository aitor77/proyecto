import sys
from ventana2 import *
from modificar import *

LISTA = []

class MiFormulario(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.enviar, QtCore.SIGNAL("clicked()"), self.aniadir)
        self.connect(self.ui.enviar2, QtCore.SIGNAL("clicked()"), self.mandar)
        self.show()

    def aniadir(self):
        if len(self.ui.usuario.text())!=0:
            a = self.ui.usuario.text()
            if len(self.ui.clave.text())!=0:
                b = self.ui.clave.text()
                # aqui codigo de la base de datos
                self.agregar(self, a, b)

                self.ui.usuario.clear()
                self.ui.clave.clear()

    def mandar(self):
        if len(self.ui.usuario2.text())!=0:
            a = self.ui.usuario2.text()
            if len(self.ui.archivo.text())!=0:
                b = self.ui.archivo.text()
                if self.ui.guardar.isChecked()== True:
                # aqui codigo de la base de datos
                    self.agregar1(self,a,b)
                if self.ui.encriptar.isChecked()==True:
                # codigo para encriptar el archivo

                    LISTA.append(b)
                if self.ui.encriptar.isChecked() == False and self.ui.guardar.isChecked()== False:
                    LISTA.append(b)
                self.ui.usuario2.clear()
                self.ui.archivo.clear()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MiFormulario()
    sys.exit(app.exec_())