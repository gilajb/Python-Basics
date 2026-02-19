temp = float(input("Enter room temperature in degree Celsius: "))

if temp == 25:
    print("Normal")

elif temp > 30:
    print("Too high")

elif temp < 21:
    print("Too low")

else:
    print("Normal")