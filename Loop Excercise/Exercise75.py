m= int(input())
n= int(input())
if m>n:
    min = n
else:
    min=m
while min >0:
    if min == 1:
        print(f"{min} là UCNN của {m} và {n}")  
        break  
    if m % min==0 and n % min==0:
        print(f"{min} là UCNN của {m} và {n}")
        break
    min-=1

    

