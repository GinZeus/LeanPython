import json

CuaHang = {
    "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
    "Áo giáp": {"Giá cả": 200, "Số lượng": 4}
}

# x =  '{ "name":"John", "age":30, "city":"New York"}'

# y = json.loads(x)
# z = json.dumps(CuaHang, ensure_ascii=False)

# print(z)


# with open ("CuaHang.json", "w", encoding="utf-8") as f:
#     json.dump(CuaHang, f, ensure_ascii=False, indent=3)



try:
    with open ("CuaHang1.json", "r", encoding="utf-8") as f:
        du_lieu_json = json.load(f)

    print(du_lieu_json["Kiếm sắt"])
    print(type(du_lieu_json))
except(Exception):
    print("Lỗi rồi thực hiện lại đi")


Tui = 5000

CuaHang = {
    "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
    "Áo giáp": {"Giá cả": 200, "Số lượng": 4},
    "Dây chuyền": {"Giá cả": 100, "Số lượng": 10}
}

Balo = {}

with open ("Tui.json", "w", encoding="utf-8") as f:
    json.dump(Tui, f, ensure_ascii=False, indent=3)

# print(du_lieu_xephang["1"])
