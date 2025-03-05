# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
num1 = float(input('1st Number: '))
num2 = float(input('2nd Number: '))

if num1>num2:
    print(num2)
elif num2>num1:
    print(num1)
else:
    print ("Equal")