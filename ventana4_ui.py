# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 216)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"Lucida Console\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 101, 31))
        self.label.setObjectName("label")
        self.Tiempo = QtWidgets.QTextEdit(self.centralwidget)
        self.Tiempo.setGeometry(QtCore.QRect(160, 80, 131, 31))
        self.Tiempo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Tiempo.setObjectName("Tiempo")
        self.AceptarT = QtWidgets.QPushButton(self.centralwidget)
        self.AceptarT.setGeometry(QtCore.QRect(120, 150, 141, 31))
        self.AceptarT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AceptarT.setObjectName("AceptarT")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Tiempo", "Tiempo"))
        self.label.setText(_translate("MainWindow", "Tiempo"))
        self.AceptarT.setText(_translate("MainWindow", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

