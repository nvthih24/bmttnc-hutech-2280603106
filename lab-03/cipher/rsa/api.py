from flask import Flask, request, jsonify
from cipher.rsa.rsa_cipher import RSACipher

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['POST'])
def generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/rsa/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    message = data.get('message')
    key_type = data.get('key_type')
    private_key, public_key = rsa_cipher.get_keys()
    if key_type == 'public':
        rsa_cipher.set_key(public_key)
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'})
    encrypted_message = rsa_cipher.encrypt(message, key_type)
    return jsonify({'encrypted_message': encrypted_message})

@app.route('/api/rsa/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    ciphertext_hex = data.get('ciphertext')
    key_type = data.get('key_type')
    private_key, public_key = rsa_cipher.get_keys()
    if key_type == 'public':
        key_type = public_key
    elif key_type == 'private':
        key_type = private_key
    else:
        return jsonify({'error': 'Invalid key type'})
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key_type)
    return jsonify({'decrypted_message': decrypted_message})

@app.route('/api/rsa/sign', methods=['POST'])
def sign():
    data = request.get_json()
    message = data.get('message')
    private_key, _ = rsa_cipher.get_keys()
    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/rsa/verify', methods=['POST'])
def verify():
    data = request.get_json()
    message = data.get('message')
    signature_hex = data.get('signature')
    public_key, _ = rsa_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({'verified': verified})

if __name__ == '__main__':
    app.run(host="0.0.0.0", post=5000, debug=True)