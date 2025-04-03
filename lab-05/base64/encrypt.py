import base64

def main():
    input_string = input("Enter the string to encode: ")

    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")

    with open("encoded.txt", "w") as file:
        file.write(encoded_string)

    print(f"Đã mã hóa chuỗi và lưu vào file 'data.txt'")

if __name__ == "__main__":
    main()