Tui = 500
CuaHang = ["Kiếm sắt", "Mũ sắt", "Dây chuyền", "Kiếm"]
GiaTien = [500, 200, 100]

Balo = []


#Người chơi nhập món mình muốn mua, hệ thống sẽ phải tính trừ tiền và thêm vào balo hoặc thông báo cho người chơi nếu đủ tiền. 
# Nếu không tìm thấy sẽ phải trả không tìm thấy sản phẩm. Và kết thúc trò chơi
# Gợi ý: sử dụng while để tạo vòng lặp, sử dụng biến isEnough để thoát khỏi vòng lặp

print(f"Đang có {Tui} xu")
print(f"Cửa hàng đang có {CuaHang}")
print(f"Balo đang có {Balo}")

isEnough = True

while (isEnough):
    print(f"Cửa hàng đang có {CuaHang}")
    mon_muon_mua = input("Bạn muốn mua: ")

    if mon_muon_mua in CuaHang:
        print("Có trong cửa hàng")

        viTriVatpham = CuaHang.index(mon_muon_mua)
        giaCa = GiaTien[viTriVatpham]
        print(f"Vị trí vật phẩm là {viTriVatpham}")
        print(f"Giá vật phẩm là {giaCa}")

        if (Tui >= giaCa):
            Balo.append(mon_muon_mua)
            Tui -= giaCa
            CuaHang.remove(mon_muon_mua)
            # GiaTien.remove(giaCa)
            print(f"Bạn còn {Tui} xu")
        else:
            print("Bạn tiền rồi, hãy nạp thêm")
            isEnough = False

    else:
        isEnough = False
        print("Sản phẩm không có trong cửa hàng")

