def lam_tron_tien(amount):
    return round(amount * 20) / 20

tong_gia = 0

while True:
    gia_nhap = input("Nhập giá của một mặt hàng (hoặc nhấn Enter để kết thúc): ")

    if gia_nhap == '':
        break

    try:
        gia = float(gia_nhap)
        tong_gia += gia  
    except ValueError:
        print("Vui lòng nhập một giá hợp lệ.")

print(f"Tổng giá của các mặt hàng: {tong_gia:.2f} đồng")

so_tien_can_tra = lam_tron_tien(tong_gia)

print(f"Số tiền cần trả khi thanh toán bằng tiền mặt: {so_tien_can_tra:.2f} đồng")