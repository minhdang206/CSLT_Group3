import math

def khoang_cach(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

chu_vi = 0
x_dau, y_dau = None, None
x_truoc, y_truoc = None, None

print("Nhập phần x của tọa độ:")
x_nhap = input()
if x_nhap == '':
    exit()
x = float(x_nhap)

print("Nhập phần y của tọa độ:")
y = float(input())

x_dau, y_dau = x, y
x_truoc, y_truoc = x, y

while True:
    print("Nhập phần x của tọa độ (để trống để kết thúc):")
    x_nhap = input()
    if x_nhap == '':
        break
    x = float(x_nhap)

    print("Nhập phần y của tọa độ:")
    y = float(input())

    chu_vi += khoang_cach(x_truoc, y_truoc, x, y)
    x_truoc, y_truoc = x, y

chu_vi += khoang_cach(x_truoc, y_truoc, x_dau, y_dau)

print(f"Chu vi của đa giác đó là {chu_vi:.15f}")
