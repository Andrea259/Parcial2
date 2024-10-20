import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Primera Ventana")
        self.setGeometry(300, 300, 300, 200)

        # Creamos un botón
        self.boton = QPushButton("mostrar texto", self)
        self.boton.setGeometry(100, 80, 100, 30)
        self.boton.clicked.connect(self.mostrar_mensaje)

        # Creamos una etiqueta que inicialmente esta oculta
        self.etiqueta = QLabel("Tengo hambre:(", self)
        self.etiqueta.setGeometry(100, 120, 100, 30)
        self.etiqueta.hide()

    def mostrar_mensaje(self):
        self.etiqueta.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())