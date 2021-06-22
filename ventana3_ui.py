# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 208)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 12pt \"Lucida Console\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 71, 31))
        self.label_2.setObjectName("label_2")
        self.Nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(150, 40, 141, 31))
        self.Nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nombre.setObjectName("Nombre")
        self.Apellido = QtWidgets.QTextEdit(self.centralwidget)
        self.Apellido.setGeometry(QtCore.QRect(150, 90, 141, 31))
        self.Apellido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Apellido.setObjectName("Apellido")
        self.Registrar = QtWidgets.QPushButton(self.centralwidget)
        self.Registrar.setGeometry(QtCore.QRect(120, 140, 131, 31))
        self.Registrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Registrar.setObjectName("Registrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Registro", "Registro"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.Registrar.setText(_translate("MainWindow", "Registrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

