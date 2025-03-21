from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    print(request.form)
    text = request.form['inputPlainText']  # Corrected field name
    key = int(request.form['inputKey'])  # Updated to match the form field name
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])  # Updated to match the form field name
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)