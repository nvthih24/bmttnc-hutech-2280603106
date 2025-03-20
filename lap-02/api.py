from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caeser_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caeser_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = caeser_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = caeser_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text}),

# VIGENERE CIPHER ALGORITHM
vigener_cipher = VigenereCipher('KEY')

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    encrypted_text = vigener_cipher.vignere_cipher(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    decrypted_text = vigener_cipher.vignere_decipher(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)