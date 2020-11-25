grade = eval(input("Enter student grade: "))

if grade > 101:
    print("Invalid grade!!!")
elif grade >=80:
    print('A')
elif grade >= 70 and grade <80 :
    print('B')
elif grade >= 60 and grade <70 :
    print('C')
elif grade >= 50 and grade < 60:
    print('D')
else:
    print('F')
