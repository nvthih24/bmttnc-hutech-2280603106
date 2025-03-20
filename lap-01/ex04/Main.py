from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1==1):
    print("1. Nhap sinh vien")
    print("2. Cap nhat sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien theo ID")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    choice = int(input("Nhap lua chon: "))
    if (choice == 1):
        qlsv.nhapSinhVien()
    elif (choice == 2):
        ID = int(input("Nhap ID sinh vien can cap nhat: "))
        qlsv.updateSinhVien(ID)
    elif (choice == 3):
        ID = int(input("Nhap ID sinh vien can xoa: "))
        qlsv.deleteSinhVien(ID)
    elif (choice == 4):
        qlsv.sortByID()
    elif (choice == 5):
        qlsv.sortByName()
        qlsv.showSinhVien(qlsv.getListSinhVien())
    elif (choice == 6):
        qlsv.sortByDiemTB()
        qlsv.showSinhVien(qlsv.getListSinhVien())
    elif (choice == 7):
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.showSinhVien(qlsv.getListSinhVien())
    elif (choice == 0):
        break
    else:
        print("Lua chon khong hop le")
    print("")
