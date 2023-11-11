tuoi_nguoi=int(input('Tuoi nguoi: '))
if tuoi_nguoi < 0:
    print("Khong hop le")
if tuoi_nguoi <= 2:
    tuoi_cho = tuoi_nguoi * 10.5
else:
    tuoi_cho = 2 * 10.5 + (tuoi_nguoi - 2) * 4
print(f'Tuoi cho: {tuoi_cho}')
