# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'ventana5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(278, 179)
        MainWindow.setStyleSheet("background-color: rgb(255, 187, 92);\n"
"font: 12pt \"Lucida Console\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AceptarC = QtWidgets.QPushButton(self.centralwidget)
        self.AceptarC.setGeometry(QtCore.QRect(100, 130, 91, 31))
        self.AceptarC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AceptarC.setObjectName("AceptarC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 201, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 31, 21))
        self.label_3.setObjectName("label_3")
        self.CordenadaN = QtWidgets.QTextEdit(self.centralwidget)
        self.CordenadaN.setGeometry(QtCore.QRect(90, 70, 51, 31))
        self.CordenadaN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CordenadaN.setObjectName("CordenadaN")
        self.CooordenadaM = QtWidgets.QTextEdit(self.centralwidget)
        self.CooordenadaM.setGeometry(QtCore.QRect(180, 70, 51, 31))
        self.CooordenadaM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CooordenadaM.setObjectName("CooordenadaM")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Tablero", "Tablero"))
        self.AceptarC.setText(_translate("MainWindow", "Aceptar"))
        self.label.setText(_translate("MainWindow", "Tamaño del tablero"))
        self.label_2.setText(_translate("MainWindow", "n"))
        self.label_3.setText(_translate("MainWindow", "m"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

