import hashlib

def calulate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = calulate_md5(input_string)

print(f"MD5 hash của chuỗi '{input_string}' là: {md5_hash}")