import hashlib

def calculate_sha256(data):
    """Calculate the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("Enter the data to hash: ")
hash_result = calculate_sha256(data_to_hash)
print(f"SHA-256 hash: {hash_result}")