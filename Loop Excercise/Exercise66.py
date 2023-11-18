# Bảng chuyển đổi từ điểm chữ sang điểm số
diem_danh_gia = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'F': 0.0
}

tong_diem = 0
so_luong = 0

# Nhập điểm từ người dùng cho đến khi nhập một dòng trống
while True:
    diem_chu = input("Nhập điểm chữ (hoặc nhấn Enter để kết thúc): ").strip().upper()

    # Kiểm tra dòng trống để thoát khỏi vòng lặp
    if diem_chu == '':
        break

    # Tính điểm số và cộng vào tổng điểm
    tong_diem += diem_danh_gia.get(diem_chu, 0)
    so_luong += 1

# Tính điểm trung bình (GPA)
if so_luong > 0:
    diem_trung_binh = tong_diem / so_luong
    print(f"Điểm trung bình (GPA) là: {diem_trung_binh:.1f}")
else:
    print("Không có điểm nào được nhập.")
