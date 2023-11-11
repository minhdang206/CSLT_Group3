a=int(input())
b=int(input())
c=int(input())
if a == b==c:
    print("equilateral triangle")
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
    print("isosceles triangle")
else:
    print("scalene triangle")
        