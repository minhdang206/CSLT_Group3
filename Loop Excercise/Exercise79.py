n = int(input())
max=n
i=0
update=0
while i < 10:
    a = int(input())
    if a > max:
        max = a
        update+=1
    i+=1
print("Số lớn nhất là",max)
print("số lần update là:", update)