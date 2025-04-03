from Crypto.Hash import SHA3_256

def sh3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Enter the text to hash: ").encode('utf-8')
    hash_value = sh3(text)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print(f"SHA3-256 hash: {hash_value.hex()}")

if __name__ == "__main__":
    main()
