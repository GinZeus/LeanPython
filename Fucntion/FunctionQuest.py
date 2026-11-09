# Balo.json, khi vòa game thì hỏi xem có load save cũ hay không (Y/N) No thì balo rỗng (gợi ý dùng os.path.exists(...) check tồn tại)
# mua bán xong thì save trong Balo.json
# xuất sản phẩm tồn kho trong cửa hàng
# nhập hàng vào cửa hàng


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
    return True


# ==========================================
# VÒNG LẶP CHÍNH CỦA GAME (MAIN LOOP)
# ==========================================
def main():
    while True:
        HienThiMenu()
        print("\nCHỌN CHỨC NĂNG:")
        print("1. Mua vật phẩm")
        print("2. Bán vật phẩm")
        print("3. Thoát")

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
            print("Cảm ơn bạn đã ghé thăm cửa hàng. Tạm biệt dũng sĩ!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại!")


if __name__ == "__main__":
    main()