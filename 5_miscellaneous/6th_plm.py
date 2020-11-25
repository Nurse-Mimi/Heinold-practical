from random import randint
count = 0

for i in range(10000):
    num = randint(1, 100) 
    if num%12==0:
        count=count+1
        print('Number of multiples of 12:', count)
        print(' ')

print('!')
print('Number of multiples of 12:', count)
