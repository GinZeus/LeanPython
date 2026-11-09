import json
import csv
import os

FILE_BALO = "Balo.json"
FILE_TON_KHO = "ton_kho.csv"
FILE_NHAP_HANG = "nhap_hang.csv"


# ==========================================
# 1. CLASS QUÁI VẬT
# ==========================================
class QuaiVat:
    def __init__(self, ten, mau, sat_thuong, vang_roi):
        self.ten = ten
        self.mau = mau
        self.mau_goc = mau
        self.sat_thuong = sat_thuong
        self.vang_roi = vang_roi

    def hien_thi(self):
        print(f"👾 [{self.ten}] | ❤️ HP: {self.mau}/{self.mau_goc} | ⚔️ ATK: {self.sat_thuong} | 💰 Rớt: {self.vang_roi} vàng")

    def bi_danh(self, luong_sat_thuong):
        self.mau -= luong_sat_thuong
        if self.mau < 0:
            self.mau = 0

    def hoi_sinh(self):
        self.mau = self.mau_goc


# ==========================================
# 2. CLASS CỬA HÀNG
# ==========================================
class CuaHang:
    def __init__(self):
        self.kho_hang = {
            "Kiếm sắt": {"Giá cả": 500, "Số lượng": 5},
            "Áo giáp": {"Giá cả": 200, "Số lượng": 4},
            "Dây chuyền": {"Giá cả": 100, "Số lượng": 10}
        }
        self.ten_cot = ["Tên vật phẩm", "Giá cả", "Số lượng"]

    def hien_thi_shop(self):
        print("--- 🏪 DANH SÁCH VẬT PHẨM TRONG CỬA HÀNG ---")
        print(f"{'Tên vật phẩm':<15} | {'Đơn giá':<10} | {'Tồn kho':<10}")
        print("-" * 45)
        for vatPham, thongTin in self.kho_hang.items():
            print(f"{vatPham:<15} | {thongTin['Giá cả']:<10} | {thongTin['Số lượng']:<10}")

    def xuat_ton_kho_csv(self):
        # TODO 1: Dùng csv.DictWriter để xuất self.kho_hang ra file ton_kho.csv
        pass

    def nhap_hang_tu_csv(self):
        # TODO 2: Dùng csv.DictReader đọc file nhap_hang.csv để cộng thêm hàng vào self.kho_hang
        pass


# ==========================================
# 3. CLASS NHÂN VẬT
# ==========================================
class NhanVat:
    def __init__(self, ten="Dũng Sĩ"):
        self.ten = ten
        self.mau = 100
        self.suc_manh = 30
        self.tui = 5000
        self.balo = {}

    def hien_thi_thong_tin(self):
        print("\n" + "=" * 45)
        print(f"🦸 NHÂN VẬT: {self.ten} | ❤️ HP: {self.mau} | ⚔️ ATK: {self.suc_manh}")
        print(f"💰 SỐ TIỀN HIỆN CÓ: {self.tui} vàng")
        print("--- 🎒 VẬT PHẨM TRONG BA LÔ ---")
        if not self.balo:
            print("(Ba lô đang trống)")
        else:
            for vatPham, soLuong in self.balo.items():
                print(f"- {vatPham}: {soLuong} cái")
        print("=" * 45)

    def luu_balo(self):
        # TODO 3: Lưu {"Tui": self.tui, "Balo": self.balo, "Mau": self.mau} vào file Balo.json
        pass

    def tai_balo(self):
        # TODO 4: Dùng os.path.exists(FILE_BALO) kiểm tra, hỏi (Y/N) để load lại self.tui, self.balo, self.mau
        pass

    def mua_vat_pham(self, shop, vatPham, soLuong):
        # TODO 5: Viết logic mua hàng từ shop.kho_hang, trừ self.tui, thêm vào self.balo rồi gọi self.luu_balo()
        pass

    def ban_vat_pham(self, shop, vatPham, soLuong):
        # TODO 6: Viết logic bán hàng từ self.balo, cộng tiền vào self.tui, hoàn kho shop.kho_hang rồi gọi self.luu_balo()
        pass

    def tan_cong(self, quai_vat):
        # TODO 7: Chém quai_vat mất self.suc_manh máu.
        # Nếu quái chết (mau == 0): cộng quai_vat.vang_roi vào self.tui, gọi quai_vat.hoi_sinh() và self.luu_balo()
        # Nếu quái chưa chết: quái cắn lại làm self.mau giảm đi quai_vat.sat_thuong
        pass


# ==========================================
# 4. VÒNG LẶP CHÍNH (MAIN LOOP)
# ==========================================
def main():
    shop = CuaHang()
    nguoi_choi = NhanVat("Dũng Sĩ")
    slime = QuaiVat("Slime Rừng", mau=50, sat_thuong=10, vang_roi=300)

    nguoi_choi.tai_balo()

    while True:
        nguoi_choi.hien_thi_thong_tin()
        shop.hien_thi_shop()

        print("\nCHỌN CHỨC NĂNG:")
        print("1. Mua vật phẩm")
        print("2. Bán vật phẩm")
        print("3. Đi đánh Slime Rừng kiếm vàng")
        print("4. Xuất tồn kho ra CSV (DictWriter)")
        print("5. Nhập hàng từ CSV (DictReader)")
        print("6. Thoát")

        luaChon = input("Nhập lựa chọn của bạn (1-6): ").strip()

        if luaChon == "1":
            tenMon = input("Nhập tên vật phẩm muốn mua: ").strip()
            try:
                soLuong = int(input("Nhập số lượng muốn mua: "))
                nguoi_choi.mua_vat_pham(shop, tenMon, soLuong)
            except ValueError:
                print("❌ Số lượng phải là số nguyên!")

        elif luaChon == "2":
            tenMon = input("Nhập tên vật phẩm muốn bán: ").strip()
            try:
                soLuong = int(input("Nhập số lượng muốn bán: "))
                nguoi_choi.ban_vat_pham(shop, tenMon, soLuong)
            except ValueError:
                print("❌ Số lượng phải là số nguyên!")

        elif luaChon == "3":
            nguoi_choi.tan_cong(slime)

        elif luaChon == "4":
            shop.xuat_ton_kho_csv()

        elif luaChon == "5":
            shop.nhap_hang_tu_csv()

        elif luaChon == "6":
            print("Cảm ơn bạn đã ghé thăm cửa hàng. Tạm biệt dũng sĩ!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại!")


if __name__ == "__main__":
    main()