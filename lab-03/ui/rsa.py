# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "C:/Users/HP/AppData/Local/Programs/Python/Python39/Lib/site-packages/PyQt5/Qt/plugins/platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_rsacipher = QtWidgets.QLabel(self.centralwidget)
        self.lbl_rsacipher.setGeometry(QtCore.QRect(230, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rsacipher.setFont(font)
        self.lbl_rsacipher.setObjectName("lbl_rsacipher")
        self.btn_generatekeys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generatekeys.setGeometry(QtCore.QRect(410, 30, 93, 28))
        self.btn_generatekeys.setObjectName("btn_generatekeys")
        self.lbl_plaintext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plaintext.setGeometry(QtCore.QRect(20, 90, 71, 16))
        self.lbl_plaintext.setObjectName("lbl_plaintext")
        self.lbl_ciphertext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ciphertext.setGeometry(QtCore.QRect(20, 280, 71, 16))
        self.lbl_ciphertext.setObjectName("lbl_ciphertext")
        self.lbl_signature = QtWidgets.QLabel(self.centralwidget)
        self.lbl_signature.setGeometry(QtCore.QRect(460, 280, 61, 16))
        self.lbl_signature.setObjectName("lbl_signature")
        self.lbl_information = QtWidgets.QLabel(self.centralwidget)
        self.lbl_information.setGeometry(QtCore.QRect(440, 90, 81, 16))
        self.lbl_information.setObjectName("lbl_information")
        self.txt_plaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(100, 90, 311, 171))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_ciphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(100, 280, 311, 171))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.txt_signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(530, 280, 311, 171))
        self.txt_signature.setObjectName("txt_signature")
        self.txt_information = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_information.setGeometry(QtCore.QRect(530, 90, 311, 171))
        self.txt_information.setObjectName("txt_information")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(120, 480, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(300, 480, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(550, 480, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(730, 480, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_rsacipher.setText(_translate("MainWindow", "RSA CIPHER"))
        self.btn_generatekeys.setText(_translate("MainWindow", "Generate Keys"))
        self.lbl_plaintext.setText(_translate("MainWindow", "Plain Text:"))
        self.lbl_ciphertext.setText(_translate("MainWindow", "Cipher Text:"))
        self.lbl_signature.setText(_translate("MainWindow", "Signature:"))
        self.lbl_information.setText(_translate("MainWindow", "Imformation:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
