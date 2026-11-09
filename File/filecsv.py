# import csv

# du_lieu_bang = [
#     ["Tên vật phẩm", "Giá cả", "Số lượng"],
#     ["Kiếm sắt", 500, 5],
#     ["Áo giáp", 200, 4],
#     ["Dây chuyền", 100, 10]
# ]

# # with open("kho_hang1.csv", "w", encoding="utf-8-sig", newline="") as f:
# #     but_ghi = csv.writer(f)

# #     but_ghi.writerows(du_lieu_bang)
import csv

with open("kho_hang1.csv", "r", encoding="utf-8-sig") as f:
    doc = csv.reader(f)

    tieu_de = next(doc)
    print(tieu_de)

    for dong in doc:
        ten = dong[0]
        gia = int(dong[1]) 
        so_luong = int(dong[2])

        print(type(dong))
        
        thanh_tien = gia * so_luong
        print(f"- {ten}: {gia} vàng x {so_luong} cái = {thanh_tien} vàng")


import csv

CuaHang = {
    "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
    "Áo giáp": {"Giá cả": 200, "Số lượng": 4},
    "Dây chuyền": {"Giá cả": 100, "Số lượng": 10}
}


# with open("Cuahang.csv", "w", encoding="utf-8-sig", newline="") as f:
#     ten_cac_cot = ["Tên vật phẩm", "Giá cả", "Số lượng", "Tổng giá trị"]

#     but_ghi = csv.DictWriter(f, fieldnames=ten_cac_cot)
#     but_ghi.writeheader()

#     for ten_sp, thong_tin in CuaHang.items():
#         gia = thong_tin["Giá cả"]
#         sl = thong_tin["Số lượng"]
#         but_ghi.writerow({
#             "Tên vật phẩm": ten_sp,
#             "Giá cả": gia,
#             "Số lượng": sl,
#             "Tổng giá trị": gia * sl
#         })


# with open("Cuahang.csv", "r", encoding="utf-8-sig") as f:
#     bo_doc = csv.DictReader(f)

#     for dong in bo_doc:
#         print(dong["Tên vật phẩm"])
#         print(type(dong))


import os

print(os.path.exists("CuaHang1.json"))


