# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os 
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtPlain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtPlain.setGeometry(QtCore.QRect(130, 60, 451, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtPlain.setFont(font)
        self.txtPlain.setObjectName("txtPlain")
        self.txtCipher = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtCipher.setGeometry(QtCore.QRect(130, 270, 451, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtCipher.setFont(font)
        self.txtCipher.setObjectName("txtCipher")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(130, 420, 111, 31))
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(480, 420, 101, 31))
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.txtSig = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtSig.setGeometry(QtCore.QRect(756, 270, 431, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtSig.setFont(font)
        self.txtSig.setObjectName("txtSig")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnVerify = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerify.setGeometry(QtCore.QRect(1060, 420, 101, 31))
        self.btnVerify.setObjectName("btnVerify")
        self.txtInfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtInfo.setGeometry(QtCore.QRect(756, 60, 431, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtInfo.setFont(font)
        self.txtInfo.setObjectName("txtInfo")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 270, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnSign = QtWidgets.QPushButton(self.centralwidget)
        self.btnSign.setGeometry(QtCore.QRect(756, 420, 111, 31))
        self.btnSign.setObjectName("btnSign")
        self.btnGenKeys = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenKeys.setGeometry(QtCore.QRect(730, 10, 111, 31))
        self.btnGenKeys.setObjectName("btnGenKeys")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1219, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Cipher"))
        self.label.setText(_translate("MainWindow", "Plain text:"))
        self.label_2.setText(_translate("MainWindow", "Cipher text:"))
        self.label_3.setText(_translate("MainWindow", "RSA CIPHER"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.btnVerify.setText(_translate("MainWindow", "Verify"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.btnSign.setText(_translate("MainWindow", "Sign"))
        self.btnGenKeys.setText(_translate("MainWindow", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
