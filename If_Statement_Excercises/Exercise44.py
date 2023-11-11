# Nhập tháng và ngày từ người dùng
month = input("Nhập tháng (ví dụ January): ").capitalize()
day = int(input("Nhập ngày (ví dụ 1): "))

# Tạo một từ điển cho các ngày lễ cố định
holidays = {
    "January 1": "New Year's Day",
    "July 1": "Canada Day",
    "December 25": "Christmas Day",
}

# Kiểm tra xem ngày nhập vào có phù hợp với ngày lễ nào không
date_key = f"{month} {day}"
if date_key in holidays:
    holiday_name = holidays[date_key]
    print(f"{month} {day} là {holiday_name}.")
else:
    print(f"{month} {day} không phù hợp với ngày lễ cố định nào.")
