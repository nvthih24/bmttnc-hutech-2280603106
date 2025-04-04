from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caeser_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caeser_encrypt():
    try:
        data = request.get_json()
        plain_text = data.get('plain_text')
        key = int(data.get('key'))
        
        if not plain_text or not key:
            return jsonify({"error": "plain_text and key are required"}), 400
        
        encrypted_text = caeser_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500  # Trả về lỗi server nếu có ngoại lệ

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        # Lấy dữ liệu từ body của request
        data = request.get_json()
        cipher_text = data.get('cipher_text')
        key = int(data.get('key'))

        # Giả sử bạn đã có phương thức decrypt_text trong lớp CaesarCipher
        decrypted_text = caeser_cipher.decrypt_text(cipher_text, key)

        # Trả về phản hồi dưới dạng tuple (body, status)
        return jsonify({'decrypted_message': decrypted_text}), 200

    except Exception as e:
        # Trả về lỗi nếu có lỗi xảy ra trong quá trình xử lý
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

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

# RAIL FENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = railfence_cipher.rail_fence_cipher(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = railfence_cipher.rail_fence_decipher(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    key = data.get('key')
    matrix = playfair_cipher.create_matrix(key)
    return jsonify({'encrypted_message': matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    matrix = playfair_cipher.create_matrix(key)
    encrypted_text = playfair_cipher.encrypt_text(plain_text, matrix)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    matrix = playfair_cipher.create_matrix(key)
    decrypted_text = playfair_cipher.decrypt_text(cipher_text, matrix)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)