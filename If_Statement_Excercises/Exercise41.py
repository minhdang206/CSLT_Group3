p = {   "C4": 261.63,
        "D4": 293.66,
        "E4": 329.63,
        "F4": 349.23,
        "G4": 392.00,
        "A4": 440.00,
        "B4": 493.88
    }
d=0
a = input()
for k in p:
    if a[0] == k[0]:
        gt = p[k] * (2 ** (int(a[1]) - int(k[1])))
        print(f"Tần số của {a} của  {gt} Hz")
        d+=1
        break 
if d==0:
    print("Khong hop le")



