# CuaHang = {
#     "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
#     "Áo giáp": {"Giá cả": 200, "Số lượng": 4}
# }

# # Thử ghi vào file .txt
# with open("save_thu.txt", "w", encoding="utf-8") as f:
#     # f.write(CuaHang) -> Sẽ báo lỗi TypeError: write() argument must be str, not dict
#     f.write(str(CuaHang))  # Phải ép sang chuỗi mới ghi được


# with open("save_thu.txt", "r", encoding="utf-8") as f:
#     du_lieu_doc_len = f.read()

# print("Dữ liệu đọc lên:", du_lieu_doc_len)
# print("Kiểu dữ liệu:", type(du_lieu_doc_len)) 
# Kết quả: <class 'str'> !!

# Thử lấy giá của Kiếm sắt:
# print(du_lieu_doc_len["Kiếm sắt"]) 
# BÁO LỖI NGAY: TypeError: string indices must be integers, not 'str'
import json

import File.HomeworkFile as HomeworkFile

CuaHang = {
    "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
    "Áo giáp": {"Giá cả": 200, "Số lượng": 4}
}

# with open("save.json", "w", encoding="utf-8") as f:
#     json.dump(CuaHang,f,ensure_ascii=False,indent=3)

with open("save.json", "r", encoding="utf-8") as f:
    Dulieukhoiphuc = json.load(f)

print("Kiểu dữ liệu sau khi load:", type(Dulieukhoiphuc))
print("Giá kiếm sắt:", Dulieukhoiphuc["Kiếm sắt"]["Giá cả"] + 100)
