class VatPham:
    def __init__(self, ten, gia_ca, sat_thuong):
        self.ten = ten
        self.gia_ca = gia_ca
        self.sat_thuong = sat_thuong

vk1 = VatPham("Kiếm sắt", 500, 25)
vk2 = VatPham("Cung thần", 800, 45)
# print(f"Vũ khí 1: {vk1.ten} | Giá: {vk1.gia_ca} vàng | Công: +{vk1.sat_thuong}")
# print(f"Vũ khí 2: {vk2.ten} | Giá: {vk2.gia_ca} vàng | Công: +{vk2.sat_thuong}")


class QuaiVat:
    def __init__(self, ten, mau, sat_thuong, vang_roi):
        self.ten = ten
        self.mau = mau
        self.mau_goc = mau # Lưu mốc máu tối đa ban đầu (VD: 50/50)
        self.sat_thuong = sat_thuong
        self.vang_roi = vang_roi

    def hien_thi(self):
        print(f"👾 Quái [{self.ten}] | ❤️ HP: {self.mau}/{self.mau_goc} | ⚔️ ATK:{self.sat_thuong} | 💰 Rớt: {self.vang_roi} vàng")

    def bi_danh(self, sat_thuong_nhan_vao):
        self.mau -= sat_thuong_nhan_vao

        if(self.mau<=0):
            self.mau = 0
            print(f"Đã hạ thành công quái")
        else:
            print(f"Quái còn {self.mau}/{self.mau_goc}")


# Slime1=QuaiVat("Slime xanh", 50, 5, 10)
# Rong_Lua=QuaiVat("Rồng lửa", 2500, 500, 1000)

# Rong_Lua.bi_danh(60)

class NhanVat:
    def __init__(self, ten, tui_ban_dau=5000):
        self.ten = ten
        self.mau = 100
        self.suc_manh = 100
        self.tui = tui_ban_dau # Thay thế hoàn toàn biến toàn cục Tui!
        self.balo = {} # Thay thế hoàn toàn biến toàn cục Balo!

    def xem_thong_tin(self):
        print(f"\n🦸 [{self.ten}] | ❤️ HP: {self.mau} | ⚔️ ATK: {self.suc_manh} |💰 Ví: {self.tui} vàng | 🎒 Ba lô: {self.balo}")

    def tan_cong(self, muc_tieu):
        print(f"\n⚔️ [{self.ten}] lao vào chém [{muc_tieu.ten}]!")

        muc_tieu.bi_danh(self.suc_manh)
        if(muc_tieu.mau <= 0):
            self.tui += muc_tieu.vang_roi
            print(f"Trong túi có {self.tui} xu")
        else:
            self.mau -= muc_tieu.sat_thuong
            print(f"Bạn còn {self.mau} HP")


dung_si = NhanVat("Arthur", tui_ban_dau=5000)
slime = QuaiVat("Slime Xanh", mau=50, sat_thuong=10, vang_roi=300)

dung_si.tan_cong(slime)
