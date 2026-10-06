# nhanVat = {
#     "Tên": "Steve",
#     "HP": 500,
#     "Tui": ['Kiếm', 'Mũ']
# }


# print(f"Nhân vật tên là {nhanVat['Tên']}")

# Mana = nhanVat.get('Mana',"Không  có gì hết")
# print(f"chỉ số mana {Mana}")
# print(f"Chỉ số nhân vật {nhanVat}")

# print("bị quái đánh")

# nhanVat["HP"] -=  200
# print(f"Máu của bạn còn {nhanVat['HP']}")

# nhanVat['Giáp'] = 50
# print(f"Chỉ số nhân vật {nhanVat}")

# del nhanVat["Tui"]
# print(f"Chỉ số nhân vật {nhanVat}")

# Shop = {
#     "Kiếm": {"Giá cả": 500, "Sức mạnh": 100},
#     "Áo giáp": {"Giá cả": 200, "Sức mạnh": 50},
#     "Bình máu": {"Giá cả": 50, "Sức mạnh": 10}
# }

# Shop1 = dict(San_pham=[1,2,3])
# print(Shop1)

# for sanpham in Shop.values():
#     print(f"Sản phẩm đang có {sanpham}")
    # print(f"Chi tiết sản phẩm {chi_tiet['Giá cả']}")


# San_pham_bi_xoa = Shop.popitem()

# print(f"Sản phẩm vừa bị xóa là {San_pham_bi_xoa}")
# print(f"Trong cửa hàng còn {Shop}")


cong_thuc = {"Đá": 2, "Gỗ": 2}
tui = {"Đá": 3, "Gỗ": 2, "Kim cương": 1}

isEnough = True

for nguyen_lieu, so_luong in cong_thuc.items():
    print(f"{nguyen_lieu} cần {so_luong}")
    if(so_luong > tui.get(nguyen_lieu,0)):
        print("Không đủ nguyên liệu")
        isEnough = False
    else:
        print("Đã đủ số lượng")

if(isEnough):
    for nguyen_lieu, so_luong in cong_thuc.items():
        tui[nguyen_lieu] -= so_luong
        if(tui[nguyen_lieu] == 0):
            print(f"{nguyen_lieu} Sản phẩm đã bị xóa trong túi")
            san_pham_bi_xoa = tui.pop(nguyen_lieu)
            
    tui["Rìu đá"] = 1
    print(f"Trong túi bạn có {tui}")




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
# HienThiMenu(): Lấy list sản phẩm trong cửa hàng (có thể dùng items)

