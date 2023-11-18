while True:
    n = input("Nhap 8 bit: ")
    if n == "":
        break

    if len(n) != 8:
        print("Nhap lai đung 8 bit.")
    else:
        a = n.count('1')
        if a % 2 == 0:
            print("Bit chan phai là 0")
        else:
            print("Bit chan phai là 1")
