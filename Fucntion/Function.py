nhanVat = {
    "Tên": "Steve",
    "HP": 500,
    "Tui": ['Kiếm', 'Mũ']
}


def  HienThiMenu():
    print(f'Thông tin nhân vật {nhanVat}')

def HoiMau(luongMauHoi):
    print(f"Đã hồi được {luongMauHoi} máu")

# def muaVatPham(*vatPham, soLuong):
#     if (vatPham and soLuong):
#         print(f'Bạn đã mua {vatPham} với số lượng là {soLuong}')
#     else:
#         print('Không đủ tham số truyền vào')


def danhQuai(vuKhi="Tay không", satThuong = 0):
    print(f"Bạn đã đánh quái bằng {vuKhi} với sát thương {satThuong}")

# HienThiMenu()
# HoiMau(500)
# muaVatPham(soLuong=5, vatPham="Kiếm sắt")


# def muaVatPham(tui, soTien):
#     SoTienConLai = tui - soTien
#     return SoTienConLai

def danhTrung(satThuongDauVao, chiSoGiapQuai):
    if(satThuongDauVao < chiSoGiapQuai):
        return False
    else:
        return True

Tui = 50000

# conLai = muaVatPham(500, 200)
# print(f"Số tiền còn lại {conLai}")
# tiLeDanhTrung = danhTrung(50,100)
# print(f"Tỉ lệ đánh trúng quái {tiLeDanhTrung}")

def muaVatPham(SoTien):
    global Tui
    Tui -= SoTien


# print(muaVatPham(2000))
muaVatPham(200)
print(f"Số tiền {Tui}")



#Quest: 

Tui = 5000
CuaHang = {
    "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
    "Áo giáp": {"Giá cả": 200, "Số lượng": 4},
    "Dây chuyển": {"Giá cả": 100, "Số lượng": 10}
}

Balo = {}

#Người chơi nhập món mình muốn mua, hệ thống sẽ phải tính trừ tiền và thêm vào balo hoặc thông báo cho người chơi nếu đủ tiền. 
# Nếu không tìm thấy sẽ phải trả không tìm thấy sản phẩm. Và kết thúc trò chơi
# trừ đi số lượng trong cửa hàng, thêm số lượng vào trong túi
# HienThiMenu(): Lấy list sản phẩm trong cửa hàng (có thể dùng CuaHang.item())
# MuaVatPham(vatPham, soLuong)
# BanVatPham(vatPham, soLuong)
# 3 option
# 1: Mua vật phẩm
# 2: Bán vật phẩm
# 3: Thoát

