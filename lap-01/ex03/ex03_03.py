def tao_tuple_tu_list(lst):
    return tuple(lst)
#Nhap danh sach tu nguoi dung va xu ly chuoi
input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List da nhap la: ", numbers)
print(f"Tuple tu List: {my_tuple}")
