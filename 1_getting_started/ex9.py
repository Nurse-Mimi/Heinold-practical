price_of_meal = eval(input("Input the price of your meal: "))
tip_percentage = eval(input("What percentage of your meal price do you want to leave as a tip? "))
print ("The tip percentage for your meal is ", (tip_percentage/100) * price_of_meal)
print ("Your total bill including tip is ", ((tip_percentage/100) * price_of_meal) +price_of_meal)