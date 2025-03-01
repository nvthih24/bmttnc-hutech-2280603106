def dao_nguoc_danh_sach(lst):
    return lst[::-1]

# Nhap danh sach tu nguoi dung va xu ly chuoi
input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))

# Su dung ham va in ket qua
danh_sach_dao_nguoc = dao_nguoc_danh_sach(numbers)
print(f"Danh sach dao nguoc la: {danh_sach_dao_nguoc}")
