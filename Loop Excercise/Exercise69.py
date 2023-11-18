import math

for i in range(1, 16):
    x = 0
    for j in range(i):
        x += ((-1) ** j) / (2 * j + 1)
    
    print(f"Xap xi {i}: {round(x,10)}")
