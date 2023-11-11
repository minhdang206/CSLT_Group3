denomination_to_individual = {
  "$1": "George Washington",
  "$2": "Thomas Jefferson",
  "$5": "Abraham Lincoln",
  "$10": "Alexander Hamilton",
  "$20": "Andrew Jackson",
  "$50": "Ulysses S. Grant",
  "$100": "Benjamin Franklin",
}

denomination = input("Nhập mệnh giá của một tờ tiền (ví dụ, $20): ")

# Kiểm tra mệnh giá có trong dictionary tra cứu hay không
if denomination in denomination_to_individual:
    individual = denomination_to_individual[denomination]
    print(f"Cá nhân được in trên tờ tiền {denomination} là {individual}.")
else:
    print("Không có mệnh giá tờ tiền tương ứng nào tồn tại.")