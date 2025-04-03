import hashlib

def blake2b(messgae):
    blake2b_hash = hashlib.blake2b(digest_size=64)
    blake2b_hash.update(messgae)
    return blake2b_hash.digest()

def main():
    text = input("Enter text to hash: ").encode('utf-8')
    hash_value = blake2b(text)
    print("Chuỗi văn bản đầu vào:", text.decode('utf-8'))
    print("BLAKE2b Hash:", hash_value.hex())

if __name__ == "__main__":
    main()