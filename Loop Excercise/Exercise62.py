original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

discount_pct = 60  # 60% off

print("Giá gốc   |   Giá giảm   |   Giá mới")
print("--------------------------------------------------")

for price in original_prices:
    discount_amount = price * (discount_pct / 100)
    new_price = price - discount_amount

    print(f"${price:.2f}             |   ${discount_amount:.2f}             |   ${new_price:.2f}")