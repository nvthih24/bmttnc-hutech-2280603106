import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests 

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.encrypt)
        self.ui.btn_decrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_ciphertext.setPlainText(data["encrypted_message"])
                self.show_message("Success", "Encrypted Successfully", QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Encryption failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_ciphertext.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                try:    
                    data = response.json()
                    decrypted_message = data.get('decrypted_message', '')
                    self.ui.txt_plaintext.setPlainText(decrypted_message)
                    self.show_message("Success", "Decrypted Successfully", QMessageBox.Information)
                except requests.exceptions.JSONDecodeError:
                    decrypted_message = data.get('decrypted_message', '')
            else:
                print(f"Error: {response.status_code} - {response.text}")
                self.ui.txt_plaintext.setPlainText(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            self.ui.txt_plaintext.setPlainText(f"Request failed: {e}")
                
    def show_message(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
