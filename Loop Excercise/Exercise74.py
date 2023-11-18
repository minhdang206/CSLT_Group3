print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()  

for i in range(1, 11):
    print(f"{i:2} ", end="")
    for j in range(1, 11):
        kq = i * j
        print(f"{kq:4}", end="")
    print() 
