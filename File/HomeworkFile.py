# Save.json, khi vòa game thì hỏi xem có load save cũ hay không (Y/N) No thì balo rỗng (gợi ý dùng os.path.exists(...) check tồn tại)
# mua bán xong thì save trong Balo.json
# xuất sản phẩm tồn kho trong cửa hàng
# nhập hàng vào cửa hàng
import json
import os
import csv

FILE_JSON = "SaveGame.json"
FILE_INPUT_CSV = "nhap_hang.csv"
FILE_OUTPUT_CSV = "ton_kho.csv"

# ==========================================
# KHỞI TẠO DỮ LIỆU BAN ĐẦU
# ==========================================
Tui = 5000

CuaHang = {
    "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
    "Áo giáp": {"Giá cả": 200, "Số lượng": 4},
    "Dây chuyền": {"Giá cả": 100, "Số lượng": 10}
}

Balo = {}


# ==========================================
# CÁC HÀM XỬ LÝ (FUNCTIONS)
# ==========================================
def LuuGame(Tui, Balo):
    du_lieu_ghi = {
        "Tui": Tui,
        "Balo": Balo
    }

    with open (FILE_JSON, "w", encoding="utf-8") as f:
        json.dump(du_lieu_ghi, f, ensure_ascii=False, indent=3)


def TaiGame():
    global Tui, Balo

    if os.path.exists(FILE_JSON):
        hoi = input("🔍 Tìm thấy file save Balo.json! Bạn có muốn load save cũ không? (Y/N): ").strip().upper()
        if (hoi == "Y"):
            try:
                with open (FILE_JSON, "r", encoding="utf-8") as f:
                    du_lieu_json = json.load(f)

                    Tui = du_lieu_json.get("Tui",5000)
                    Balo = du_lieu_json.get("Balo",{})

                    print(f"Tải game thành công. Túi có {Tui}, Balo có {Balo}")
            except(Exception) as e:
                print("File json lỗi. Trò chơi sẽ bắt đầu lại từ đầu")
                print(f"Lỗi {e}")
        else:
            Tui = 5000
            Balo = {}
            print("Bạn không lựa chọn tải lại game. Trò chơi sẽ bắt đầu lại từ đầu")

    else:
        print("Không tìm file save game. Trò chơi sẽ bắt đầu lại từ đầu")


def XuatTonKho(CuaHang):
    with open(FILE_OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        ten_cac_cot = ["Tên vật phẩm", "Giá cả", "Số lượng", "Tổng giá trị"]

        but_ghi = csv.DictWriter(f, fieldnames=ten_cac_cot)
        but_ghi.writeheader()

        for ten_sp, thong_tin in CuaHang.items():
            gia = thong_tin["Giá cả"]
            sl = thong_tin["Số lượng"]
            but_ghi.writerow({
                "Tên vật phẩm": ten_sp,
                "Giá cả": gia,
                "Số lượng": sl,
                "Tổng giá trị": gia * sl
            })

def TaoFileNhapHangMau():
    """Tạo sẵn file nhap_hang.csv mẫu bằng DictWriter nếu trên máy chưa có"""
    if not os.path.exists(FILE_INPUT_CSV):
        ten_cot = ["Tên vật phẩm", "Giá cả", "Số lượng"]
        du_lieu_mau = [
            {"Tên vật phẩm": "Kiếm sắt", "Giá cả": 500, "Số lượng": 10},  # Hàng đã có -> cộng dồn
            {"Tên vật phẩm": "Cung thần", "Giá cả": 800, "Số lượng": 3},   # Hàng mới -> thêm mới
            {"Tên vật phẩm": "Bình máu", "Giá cả": 50, "Số lượng": 20}     # Hàng mới -> thêm mới
        ]
        with open(FILE_INPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=ten_cot)
            writer.writeheader()
            writer.writerows(du_lieu_mau)  # Ghi cả danh sách các dict cùng lúc
        print(f"📝 (Đã tạo file mẫu '{FILE_INPUT_CSV}' bằng DictWriter để kiểm thử)")

def NhapHangTonKho():
    if not os.path.exists(FILE_INPUT_CSV):
        TaoFileNhapHangMau()

    try:
        with open(FILE_INPUT_CSV, "r", encoding="utf-8-sig") as f:
            bo_doc = csv.DictReader(f)

            for dong in bo_doc:
                vat_pham = dong["Tên vật phẩm"]
                gia_ca = int(dong["Giá cả"])
                so_luong_nhap = int(dong["Số lượng"])

                if vat_pham in CuaHang:
                    CuaHang[vat_pham]["Giá cả"] = gia_ca
                    CuaHang[vat_pham]["Số lượng"] += so_luong_nhap
                else:
                    CuaHang[vat_pham] = {"Giá cả": gia_ca, "Số lượng": so_luong_nhap}
        print("Nhập sản phẩm vào thành công")
    except (Exception) as e:
        print(f"Lỗi khi đọc file csv {e}")

def HienThiMenu():
    """Hiển thị danh mục hàng hóa trong tiệm và tình trạng người chơi"""
    print("\n" + "=" * 45)
    print(f"💰 SỐ TIỀN HIỆN CÓ: {Tui} vàng")
    print("--- 🏪 DANH SÁCH VẬT PHẨM TRONG CỬA HÀNG ---")
    print(f"{'Tên vật phẩm':<15} | {'Đơn giá':<10} | {'Tồn kho':<10}")
    print("-" * 45)
    
    # Sử dụng CuaHang.items() duyệt key và value
    for vatPham, thongTin in CuaHang.items():
        print(f"{vatPham:<15} | {thongTin['Giá cả']:<10} | {thongTin['Số lượng']:<10}")
        
    print("--- 🎒 VẬT PHẨM TRONG BA LÔ ---")
    if not Balo:
        print("(Ba lô đang trống)")
    else:
        for vatPham, soLuong in Balo.items():
            print(f"- {vatPham}: {soLuong} cái")
    print("=" * 45)


def MuaVatPham(vatPham, soLuong):
    """Xử lý mua hàng: kiểm tra tồn kho, kiểm tra tiền, trừ tiền, thêm vào balo"""
    global Tui  # Cần sửa giá trị biến int toàn cục

    # 1. Kiểm tra vật phẩm có tồn tại trong shop không
    if vatPham not in CuaHang:
        print(f"❌ Cửa hàng không bán món '{vatPham}'!")
        return False

    # 2. Kiểm tra số lượng hợp lệ và tồn kho
    if soLuong <= 0:
        print("❌ Số lượng mua phải lớn hơn 0!")
        return False

    soLuongKho = CuaHang[vatPham]["Số lượng"]
    if soLuong > soLuongKho:
        print(f"❌ Cửa hàng chỉ còn {soLuongKho} {vatPham}, không đủ để bán!")
        return False

    # 3. Tính tiền và kiểm tra khả năng thanh toán
    donGia = CuaHang[vatPham]["Giá cả"]
    tongTien = donGia * soLuong

    if Tui < tongTien:
        print(f"❌ Bạn không đủ tiền! Cần {tongTien} vàng nhưng chỉ có {Tui} vàng.")
        return False

    # 4. Thực hiện giao dịch
    Tui -= tongTien
    CuaHang[vatPham]["Số lượng"] -= soLuong

    # Cập nhật vào ba lô (nếu chưa có thì gán, có rồi thì cộng dồn)
    if vatPham in Balo:
        Balo[vatPham] += soLuong
    else:
        Balo[vatPham] = soLuong

    print(f"✅ Mua thành công {soLuong}x '{vatPham}' với giá {tongTien} vàng!")
    LuuGame(Tui, Balo)
    return True


def BanVatPham(vatPham, soLuong):
    """Xử lý bán hàng: kiểm tra đồ trong balo, trả tiền, hoàn kho"""
    global Tui

    # 1. Kiểm tra có đồ trong ba lô không
    if vatPham not in Balo or Balo[vatPham] == 0:
        print(f"❌ Trong ba lô của bạn không có món '{vatPham}'!")
        return False

    # 2. Kiểm tra số lượng muốn bán
    if soLuong <= 0:
        print("❌ Số lượng bán phải lớn hơn 0!")
        return False

    if soLuong > Balo[vatPham]:
        print(f"❌ Bạn chỉ có {Balo[vatPham]} {vatPham} trong ba lô, không đủ để bán!")
        return False

    # 3. Tính tiền bán lại (ở đây bán theo đơn giá gốc trong Cửa Hàng)
    donGia = CuaHang[vatPham]["Giá cả"]
    tongTienNhan = donGia * soLuong

    # 4. Thực hiện giao dịch
    Tui += tongTienNhan
    Balo[vatPham] -= soLuong
    if Balo[vatPham] == 0:
        del Balo[vatPham]  # Xóa khỏi ba lô nếu số lượng về 0

    CuaHang[vatPham]["Số lượng"] += soLuong

    print(f"✅ Bán thành công {soLuong}x '{vatPham}', nhận lại {tongTienNhan} vàng!")
    LuuGame(Tui, Balo)
    return True


# ==========================================
# VÒNG LẶP CHÍNH CỦA GAME (MAIN LOOP)
# ==========================================
def main():
    TaiGame()

    while True:
        HienThiMenu()
        print("\nCHỌN CHỨC NĂNG:")
        print("1. Mua vật phẩm")
        print("2. Bán vật phẩm")
        print("3. Xuất sản phẩm tồn kho")
        print("4. Nhập hàng cho cửa hàng")
        print("5. Thoát")

        luaChon = input("Nhập lựa chọn của bạn (1-3): ").strip()

        if luaChon == "1":
            tenMon = input("Nhập tên vật phẩm muốn mua: ").strip()
            try:
                soLuong = int(input("Nhập số lượng muốn mua: "))
                MuaVatPham(tenMon, soLuong)
            except ValueError:
                print("❌ Số lượng phải là số nguyên!")

        elif luaChon == "2":
            tenMon = input("Nhập tên vật phẩm muốn bán: ").strip()
            try:
                soLuong = int(input("Nhập số lượng muốn bán: "))
                BanVatPham(tenMon, soLuong)
            except ValueError:
                print("❌ Số lượng phải là số nguyên!")
        elif luaChon == "3":
            XuatTonKho(CuaHang)

        elif luaChon == "4":
            NhapHangTonKho()

        elif luaChon == "5":
            print("Cảm ơn bạn đã ghé thăm cửa hàng. Tạm biệt dũng sĩ!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại!")


if __name__ == "__main__":
    main()