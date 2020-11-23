numbers = eval(input("How may Fabonacci numbers do you wish to print?: "))
n1, n2 = 1, 1
count = 0

for i in range (0, numbers):
    if numbers == 1:
        print(n1)
    else:
        while count < numbers:
            print(n1, end= " ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
