import random
k=0
for i in range(10):
    dem=1  
    Dx=["H", "T"]
    n = random.choice(Dx)
    st=n
    d=1
    while dem<3:   
        Dx=["H", "T"]
        n = random.choice(Dx) 
        d+=1
        if n == st[len(st)-1]:
            dem+=1
            st=st+" "+n
        else:
            dem=1
            st=st+" "+n
    k+=d
    print(f"{st} ({d} flips)")
print(k/10)

        

        

    