# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_caesarcipher = QtWidgets.QLabel(self.centralwidget)
        self.lbl_caesarcipher.setGeometry(QtCore.QRect(290, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_caesarcipher.setFont(font)
        self.lbl_caesarcipher.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_caesarcipher.setAutoFillBackground(False)
        self.lbl_caesarcipher.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_caesarcipher.setObjectName("lbl_caesarcipher")
        self.lbl_plaintext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plaintext.setGeometry(QtCore.QRect(30, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_plaintext.setFont(font)
        self.lbl_plaintext.setObjectName("lbl_plaintext")
        self.lbl_key = QtWidgets.QLabel(self.centralwidget)
        self.lbl_key.setGeometry(QtCore.QRect(30, 230, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_key.setFont(font)
        self.lbl_key.setObjectName("lbl_key")
        self.lbl_ciphertext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ciphertext.setGeometry(QtCore.QRect(30, 320, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_ciphertext.setFont(font)
        self.lbl_ciphertext.setObjectName("lbl_ciphertext")
        self.txt_plaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(150, 100, 581, 87))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_key = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(150, 230, 581, 31))
        self.txt_key.setObjectName("txt_key")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(200, 460, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(530, 460, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.txt_ciphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(150, 310, 581, 87))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.lbl_caesarcipher.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.lbl_plaintext.setText(_translate("MainWindow", "Plain Text:"))
        self.lbl_key.setText(_translate("MainWindow", "Key:"))
        self.lbl_ciphertext.setText(_translate("MainWindow", "Cipher Text:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())