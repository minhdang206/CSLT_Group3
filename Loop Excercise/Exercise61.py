total = 0
count = 0

value = float(input("Nhập số (0 để dừng lại): "))

if value == 0:
    print("Không thể nhập không là giá trị đầu")
else:
    while value != 0:
        total += value
        count += 1
        value = float(input("Nhập số (0 để dừng lại): "))

    if count > 0:
        average = total / count
        print(f"Giá trị trung bình của các số đã nhập là: {average}")
    else:
        print("Không có giá trị")