temp = eval(input("Enter a temperature in Celsius: "))
if temp < -273.15:
    print("Invalid temperature due to temperature being below absolute zero.")
elif temp == -273.15:
    print("Temperature is absolut zero.")
elif temp >-273.15 and temp <0:
    print("Temperature is below freezing point.")
elif temp == 0:
    print("Temperature is at freezing point.")
elif temp >0 and temp <100:
    print("Temperature is at normal range.")
elif temp == 100:
    print("Temperature is at boiling point.")
else:
    print("Temperature is above boiling point.")