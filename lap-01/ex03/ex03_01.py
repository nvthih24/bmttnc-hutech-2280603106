def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:  # Corrected variable name from 'i' to 'num'
        if num % 2 == 0:
            tong += num
    return tong

# Nhap danh sach tu nguoi dung va xu ly chuoi
input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))

# Su dung ham va in ket qua
tong_chan = tinh_tong_so_chan(numbers)
print(f"Tong cac so chan la: {tong_chan}")