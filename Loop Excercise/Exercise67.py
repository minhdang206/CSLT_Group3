tuoi_mien_phi = 2
chi_phi_tre_em = 14.00
chi_phi_nguoi_cao_tuoi = 18.00
chi_phi_mac_dinh = 23.00

# Khởi tạo biến
tong_chi_phi = 0
cac_tuoi = []

print("Nhập tuổi của các khách (nhấn Enter sau mỗi tuổi, để trống và nhấn Enter để kết thúc):")
while True:
    tuoi_nhap = input().strip()

    # Kiểm tra dòng trống để thoát khỏi vòng lặp
    if tuoi_nhap == '':
        break

    tuoi = int(tuoi_nhap)
    cac_tuoi.append(tuoi)

# Tính tổng chi phí vào cửa dựa trên nhóm tuổi
for tuoi in cac_tuoi:
    if tuoi <= tuoi_mien_phi:
        tong_chi_phi += 0
    elif 3 <= tuoi <= 12:
        tong_chi_phi += chi_phi_tre_em
    elif tuoi >= 65:
        tong_chi_phi += chi_phi_nguoi_cao_tuoi
    else:
        tong_chi_phi += chi_phi_mac_dinh

# Hiển thị tổng chi phí vào cửa cho nhóm
print(f"Tổng chi phí vào cửa cho nhóm là: ${tong_chi_phi:.2f}")