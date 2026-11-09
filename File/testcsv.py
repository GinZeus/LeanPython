# import csv

# du_lieu_bang = [
#     ["Tên vật phẩm", "Giá cả", "Số lượng"],  # Dòng tiêu đề (Header)
#     ["Kiếm sắt", 500, 5],
#     ["Áo giáp", 200, 4],
#     ["Dây chuyền", 100, 10]
# ]

# with open("kho_hang.csv", "w", encoding="utf-8-sig", newline="") as f:
#     but_ghi = csv.writer(f)
    
#     # Cách 1: Ghi từng dòng lẻ bằng writerow(1_list)
#     # but_ghi.writerow(["Tên vật phẩm", "Giá cả", "Số lượng"])
    
#     # Cách 2: Ghi toàn bộ danh sách 2 chiều cùng lúc bằng writerows(list_2_chieu)
#     but_ghi.writerows(du_lieu_bang)

import csv

with open("kho_hang.csv", "r", encoding="utf-8-sig") as f:
    bo_doc = csv.reader(f)
    
    # Dùng hàm next() để bóc riêng dòng tiêu đề đầu tiên ra
    tieu_de = next(bo_doc)
    print("Các cột của bảng:", tieu_de)
    
    # Duyệt qua các dòng dữ liệu còn lại (mỗi dong là 1 list các chuỗi)
    tong_gia_tri_kho = 0
    for dong in bo_doc:
        ten = dong[0]
        gia = int(dong[1])       # Phải ép kiểu từ str sang int!
        so_luong = int(dong[2])  # Phải ép kiểu từ str sang int!
        
        thanh_tien = gia * so_luong
        tong_gia_tri_kho += thanh_tien
        print(f"- {ten}: {gia} vàng x {so_luong} cái = {thanh_tien} vàng")

    print(f"=> TỔNG GIÁ TRỊ TỒN KHO: {tong_gia_tri_kho} vàng")