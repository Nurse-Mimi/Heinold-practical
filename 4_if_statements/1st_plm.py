from random import randint

num = randint(1, 10)
guess = eval(input("Try guessing the number: "))
if guess==num:
    print("You guessed right!!!!")
else:
    print("aw ><, wrong guess. Try again!!!")
    print("The random number was, ", num)