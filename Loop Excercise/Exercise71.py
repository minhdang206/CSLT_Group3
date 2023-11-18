n = float(input("n="))

x = n/2.0

a = 1e-12

while abs(x * x - n) > a:
    x = (x + n / x) / 2.0

print(f"Can bac hai cua {n} xap xi = {round(x,10)}")
