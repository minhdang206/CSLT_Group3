n = input()
x = int(input())

kq = ""

for i in n:
    if i.isalpha():
        kq += chr(ord(i) + x)
    else:
        kq += i

print(kq)
