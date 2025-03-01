def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

# Nhap tuple tu nguoi dung
input_tuple = eval(input("Nhap tuple, cach nhau boi dau phay: "))
first, last = truy_cap_phan_tu(input_tuple)

print(f"Phan tu dau tien: {first}")
print(f"Phan tu cuoi cung: {last}")
