length = eval(input("Please enter a length in centimeters: "))

if length <=0:
    print("Invalid length!")
else:
    print(length, "centimeters in inches is; ", length/2.54, "inches!")
