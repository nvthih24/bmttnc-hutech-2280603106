from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (sv._id > maxId):
                    maxId = sv._id
            maxId += 1
        return maxId
    
    def soLuongSinhVien(self):
        return len(self.listSinhVien)
    
    def nhapSinhVien(self):
        svId = self.generateID()
        svName = input("Nhap ten sinh vien: ")
        svSex = input("Nhap gioi tinh: ")
        svMajor = input("Nhap nganh hoc: ")
        svDiemTB = float(input("Nhap diem trung binh: "))
        sv = SinhVien(svId, svName, svSex, svMajor, svDiemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findById(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh: ")
            major = input("Nhap nganh hoc: ")
            diemTB = float(input("Nhap diem trung binh: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại".format(ID))

    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB < 5):
            sv._hocLuc = "Yeu"
        elif (sv._diemTB < 7):
            sv._hocLuc = "Trung Binh"
        elif (sv._diemTB < 8):
            sv._hocLuc = "Kha"
        elif (sv._diemTB < 9):
            sv._hocLuc = "Gioi"
        else:
            sv._hocLuc = "Xuat Sac"

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)

    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
                    break
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findById(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def showSinhVien(self, listSV):
        print("{:<5} {:<20} {:<10} {:<20} {:<10} {:<10}".format("ID", "Ten", "Gioi Tinh", "Nganh Hoc", "Diem TB", "Hoc Luc"))
        if(len(listSV) > 0):
            for sv in listSV:
                print("{:<5} {:<20} {:<10} {:<20} {:<10} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))  
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien

