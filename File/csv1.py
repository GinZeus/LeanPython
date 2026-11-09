# import csv

# CuaHang = {
#     "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
#     "Áo giáp": {"Giá cả": 200, "Số lượng": 4},
#     "Dây chuyền": {"Giá cả": 100, "Số lượng": 10}
# }

# with open("bao_cao_shop.csv", "w", encoding="utf-8-sig", newline="") as f:
#     # 1. Định nghĩa danh sách tên các cột (fieldnames)
#     ten_cac_cot = ["Tên vật phẩm", "Giá cả", "Số lượng", "Tổng giá trị"]
    
#     # 2. Khởi tạo DictWriter
#     writer = csv.DictWriter(f, fieldnames=ten_cac_cot)
    
#     # 3. Ghi dòng tiêu đề đầu tiên
#     writer.writeheader()
    
#     # 4. Duyệt CuaHang và ghi từng dòng dạng dict
#     for ten_sp, thong_tin in CuaHang.items():
#         gia = thong_tin["Giá cả"]
#         sl = thong_tin["Số lượng"]
#         writer.writerow({
#             "Tên vật phẩm": ten_sp,
#             "Giá cả": gia,
#             "Số lượng": sl,
#             "Tổng giá trị": gia * sl
#         })

# import csv

# with open("bao_cao_shop.csv", "r", encoding="utf-8-sig") as f:
#     # DictReader tự động lấy dòng đầu tiên làm Key cho mọi dòng bên dưới!
#     reader = csv.DictReader(f)
#     for dong in reader:
#         # Mỗi 'dong' bây giờ là 1 Dictionary thực thụ:
#         # {'Tên vật phẩm': 'Kiếm sắt', 'Giá cả': '500', 'Số lượng': '5', 'Tổng giá trị': '2500'}
#         print(f"Sản phẩm: {dong['Tên vật phẩm']} | Tồn kho: {dong['Số lượng']}")

import os

print(os.path.exists('File.py'))