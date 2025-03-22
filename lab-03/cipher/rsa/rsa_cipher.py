import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class RSACipher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generatekeys.clicked.connect(self.gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.encrypt)
        self.ui.btn_decrypt.clicked.connect(self.decrypt)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.btn_verify.clicked.connect(self.verify)

    def gen_keys(self):
        url = "http://127:0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_public_key.setPlainText(data["public_key"])
                self.ui.txt_private_key.setPlainText(data["private_key"])
                self.show_message("Success", "Keys generated successfully", QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Key generation failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.show_message("Error", f"Key generation failed: {e}", QMessageBox.Warning)
            
    def encrypt(self):
        url = "http://127:0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plaintext.toPlainText(),
            "key_type": "public",
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_ciphertext.setPlainText(data["encrypted_message"])
                self.show_message("Success", "Encrypted successfully", QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Encryption failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.show_message("Error", f"Encryption failed: {e}", QMessageBox.Warning)

    def decrypt(self):
        url = "http://127:0.0.1:5000/api/rsa/decrypt"
        payload = {
            "message": self.ui.txt_ciphertext.toPlainText(),
            "key_type": "private",
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setPlainText(data["decrypted_message"])
                self.show_message("Success", "Decrypted successfully", QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Decryption failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.show_message("Error", f"Decryption failed: {e}", QMessageBox.Warning)

    def sign(self):
        url = "http://127:0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_plaintext.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_signature.setPlainText(data["signature"])
                self.show_message("Success", "Signed successfully", QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Signing failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.show_message("Error", f"Signing failed: {e}", QMessageBox.Warning)

    def verify(self):
        url = "http://127:0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_plaintext.toPlainText(),
            "signature": self.ui.txt_signature.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.show_message("Success", data["message"], QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Verification failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            self.show_message("Error", f"Verification failed: {e}", QMessageBox.Warning)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSACipher()
    window.show()
    sys.exit(app.exec_())