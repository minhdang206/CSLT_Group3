n = input("Nhap chuoi: ")
n = n.lower()
n = ''.join(filter(str.isalnum, n))  
n = n.replace(" ", "") 

x = True

for i in range(len(n) // 2):
    if n[i] != n[-i - 1]:
        x = False
        break

if x:
    print(f"'{n}' la chuoi doi xung")
else:
    print(f"'{n}' khong phai la chuoi doi xung")
