n = input("Nhap chuoi: ")
n = n.lower()
n = n.replace(" ", "")

x = True

for i in range(len(n) // 2):
    if n[i] != n[-i - 1]:
        x = False
        break

if x==True:
    print(f"'{n}' la chuoi doi xung")
else:
    print(f"'{n}' khong phai chuoi doi xung")
