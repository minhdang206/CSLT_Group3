def doC_to_doF(celsius):
    return (celsius * 9/5) + 32

print("Độ C    |    Độ F")
print("---------------------------")

for celsius in range(0, 101, 10):
    fahrenheit = doC_to_doF(celsius)
    print(f"{celsius}°C        |    {fahrenheit:.2f}°F")