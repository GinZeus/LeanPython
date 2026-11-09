import json
import csv
import os

# ==========================================
# KHỞI TẠO DỮ LIỆU BAN ĐẦU & TÊN FILE
# ==========================================
FILE_BALO = "Balo.json"
FILE_TON_KHO = "ton_kho.csv"
FILE_NHAP_HANG = "nhap_hang.csv"

Tui = 5000

CuaHang = {
    "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
    "Áo giáp": {"Giá cả": 200, "Số lượng": 4},
    "Dây chuyền": {"Giá cả": 100, "Số lượng": 10}
}

Balo = {}


# ==========================================
# CÁC HÀM XỬ LÝ FILE (JSON & CSV DẠNG DICT)
# ==========================================
def LuuBalo():
    """Lưu trạng thái Balo và Tiền vào file Balo.json sau khi mua/bán"""
    du_lieu = {
        "Tui": Tui,
        "Balo": Balo
    }
    with open(FILE_BALO, "w", encoding="utf-8") as f:
        json.dump(du_lieu, f, ensure_ascii=False, indent=4)
    print("💾 [Auto-Save] Đã lưu dữ liệu vào Balo.json!")


def TaiBalo():
    """Khi vào game, kiểm tra Balo.json bằng os.path.exists và hỏi Y/N"""
    global Tui, Balo

    if os.path.exists(FILE_BALO):
        hoi = input("🔍 Tìm thấy file save Balo.json! Bạn có muốn load save cũ không? (Y/N): ").strip().upper()
        if hoi == "Y":
            try:
                with open(FILE_BALO, "r", encoding="utf-8") as f:
                    du_lieu = json.load(f)
                    Tui = du_lieu.get("Tui", 5000)
                    Balo = du_lieu.get("Balo", {})
                print("✨ Đã load save cũ thành công!")
                return
            except Exception as e:
                print(f"⚠️ File Balo.json bị lỗi ({e}). Khởi tạo Ba lô rỗng!")
        else:
            print("🆕 Không load save cũ. Khởi tạo Ba lô rỗng!")
            Balo = {}
            Tui = 5000
    else:
        print("🌱 Chưa có file Balo.json. Bắt đầu game mới với Ba lô rỗng!")


def XuatTonKho():
    """Xuất sản phẩm tồn kho trong cửa hàng ra CSV bằng DictWriter"""
    # 1. Khai báo danh sách tên các cột (fieldnames)
    ten_cot = ["Tên vật phẩm", "Giá cả", "Số lượng"]

    with open(FILE_TON_KHO, "w", encoding="utf-8-sig", newline="") as f:
        # 2. Tạo bộ ghi DictWriter gắn với danh sách tên cột
        writer = csv.DictWriter(f, fieldnames=ten_cot)

        # 3. Tự động ghi dòng tiêu đề đầu tiên (Tên vật phẩm,Giá cả,Số lượng)
        writer.writeheader()

        # 4. Duyệt CuaHang và ghi từng dòng bằng một Dictionary
        for vatPham, thongTin in CuaHang.items():
            writer.writerow({
                "Tên vật phẩm": vatPham,
                "Giá cả": thongTin["Giá cả"],
                "Số lượng": thongTin["Số lượng"]
            })

    print(f"📊 Đã xuất tồn kho cửa hàng ra file '{FILE_TON_KHO}' bằng DictWriter!")


def TaoFileNhapHangMau():
    """Tạo sẵn file nhap_hang.csv mẫu bằng DictWriter nếu trên máy chưa có"""
    if not os.path.exists(FILE_NHAP_HANG):
        ten_cot = ["Tên vật phẩm", "Giá cả", "Số lượng"]
        du_lieu_mau = [
            {"Tên vật phẩm": "Kiếm sắt", "Giá cả": 500, "Số lượng": 10},  # Hàng đã có -> cộng dồn
            {"Tên vật phẩm": "Cung thần", "Giá cả": 800, "Số lượng": 3},   # Hàng mới -> thêm mới
            {"Tên vật phẩm": "Bình máu", "Giá cả": 50, "Số lượng": 20}     # Hàng mới -> thêm mới
        ]
        with open(FILE_NHAP_HANG, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=ten_cot)
            writer.writeheader()
            writer.writerows(du_lieu_mau)  # Ghi cả danh sách các dict cùng lúc
        print(f"📝 (Đã tạo file mẫu '{FILE_NHAP_HANG}' bằng DictWriter để kiểm thử)")


def NhapHangTuCSV():
    """Đọc file nhap_hang.csv bằng DictReader để cập nhật vào CuaHang"""
    TaoFileNhapHangMau()

    print(f"\n--- 🚚 ĐANG NHẬP HÀNG TỪ FILE '{FILE_NHAP_HANG}' ---")
    try:
        with open(FILE_NHAP_HANG, "r", encoding="utf-8-sig") as f:
            # DictReader tự động lấy dòng đầu tiên làm Key cho từng dòng bên dưới
            reader = csv.DictReader(f)

            so_loai_nhap = 0
            for dong in reader:
                # Truy cập trực tiếp qua tên cột cực kỳ rõ ràng, không cần nhớ chỉ số 0, 1, 2
                ten_sp = dong["Tên vật phẩm"].strip()
                gia_nhap = int(dong["Giá cả"])       # Ép kiểu từ str sang int
                so_luong_nhap = int(dong["Số lượng"]) # Ép kiểu từ str sang int

                # Nếu món hàng ĐÃ CÓ trong CuaHang -> Cộng dồn số lượng & cập nhật giá
                if ten_sp in CuaHang:
                    CuaHang[ten_sp]["Số lượng"] += so_luong_nhap
                    CuaHang[ten_sp]["Giá cả"] = gia_nhap
                    print(f"  + Cộng thêm {so_luong_nhap}x '{ten_sp}' (Tổng kho: {CuaHang[ten_sp]['Số lượng']})")

                # Nếu món hàng CHƯA CÓ -> Thêm key mới vào CuaHang
                else:
                    CuaHang[ten_sp] = {"Giá cả": gia_nhap, "Số lượng": so_luong_nhap}
                    print(f"  + Hàng mới: '{ten_sp}' | Giá: {gia_nhap} | Số lượng: {so_luong_nhap}")

                so_loai_nhap += 1

        print(f"✅ Hoàn tất! Đã nhập {so_loai_nhap} mặt hàng từ CSV vào Cửa Hàng.")

    except FileNotFoundError:
        print(f"❌ Không tìm thấy file '{FILE_NHAP_HANG}'!")
    except KeyError as e:
        print(f"❌ File CSV bị sai tên cột tiêu đề (Thiếu cột {e})!")
    except ValueError:
        print("❌ Lỗi dữ liệu: Cột 'Giá cả' và 'Số lượng' trong CSV phải là số nguyên!")


# ==========================================
# CÁC HÀM XỬ LÝ MUA BÁN GỐC
# ==========================================
def HienThiMenu():
    """Hiển thị danh mục hàng hóa trong tiệm và tình trạng người chơi"""
    print("\n" + "=" * 45)
    print(f"💰 SỐ TIỀN HIỆN CÓ: {Tui} vàng")
    print("--- 🏪 DANH SÁCH VẬT PHẨM TRONG CỬA HÀNG ---")
    print(f"{'Tên vật phẩm':<15} | {'Đơn giá':<10} | {'Tồn kho':<10}")
    print("-" * 45)
    
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
    global Tui

    if vatPham not in CuaHang:
        print(f"❌ Cửa hàng không bán món '{vatPham}'!")
        return False

    if soLuong <= 0:
        print("❌ Số lượng mua phải lớn hơn 0!")
        return False

    soLuongKho = CuaHang[vatPham]["Số lượng"]
    if soLuong > soLuongKho:
        print(f"❌ Cửa hàng chỉ còn {soLuongKho} {vatPham}, không đủ để bán!")
        return False

    donGia = CuaHang[vatPham]["Giá cả"]
    tongTien = donGia * soLuong

    if Tui < tongTien:
        print(f"❌ Bạn không đủ tiền! Cần {tongTien} vàng nhưng chỉ có {Tui} vàng.")
        return False

    Tui -= tongTien
    CuaHang[vatPham]["Số lượng"] -= soLuong

    if vatPham in Balo:
        Balo[vatPham] += soLuong
    else:
        Balo[vatPham] = soLuong

    print(f"✅ Mua thành công {soLuong}x '{vatPham}' với giá {tongTien} vàng!")
    LuuBalo()
    return True


def BanVatPham(vatPham, soLuong):
    global Tui

    if vatPham not in Balo or Balo[vatPham] == 0:
        print(f"❌ Trong ba lô của bạn không có món '{vatPham}'!")
        return False

    if soLuong <= 0:
        print("❌ Số lượng bán phải lớn hơn 0!")
        return False

    if soLuong > Balo[vatPham]:
        print(f"❌ Bạn chỉ có {Balo[vatPham]} {vatPham} trong ba lô, không đủ để bán!")
        return False

    if vatPham in CuaHang:
        donGia = CuaHang[vatPham]["Giá cả"]
    else:
        donGia = 100
        CuaHang[vatPham] = {"Giá cả": donGia, "Số lượng": 0}

    tongTienNhan = donGia * soLuong

    Tui += tongTienNhan
    Balo[vatPham] -= soLuong
    if Balo[vatPham] == 0:
        del Balo[vatPham]

    CuaHang[vatPham]["Số lượng"] += soLuong

    print(f"✅ Bán thành công {soLuong}x '{vatPham}', nhận lại {tongTienNhan} vàng!")
    LuuBalo()
    return True


# ==========================================
# VÒNG LẶP CHÍNH CỦA GAME (MAIN LOOP)
# ==========================================
def main():
    TaiBalo()

    while True:
        HienThiMenu()
        print("\nCHỌN CHỨC NĂNG:")
        print("1. Mua vật phẩm")
        print("2. Bán vật phẩm")
        print("3. Xuất sản phẩm tồn kho ra CSV (DictWriter)")
        print("4. Nhập hàng vào cửa hàng từ CSV (DictReader)")
        print("5. Thoát")

        luaChon = input("Nhập lựa chọn của bạn (1-5): ").strip()

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
            XuatTonKho()

        elif luaChon == "4":
            NhapHangTuCSV()

        elif luaChon == "5":
            print("Cảm ơn bạn đã ghé thăm cửa hàng. Tạm biệt dũng sĩ!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại!")


if __name__ == "__main__":
    main()