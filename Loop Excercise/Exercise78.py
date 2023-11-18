n = int(input())
i=""
while n!=0:
    a=n%2
    i=str(a)+i
    n= n//2
print(i)
