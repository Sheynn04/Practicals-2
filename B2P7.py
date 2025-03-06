# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even = []
for i in range (10):
    numbers = float(input(f"Input # {i+1}: "))
    if numbers % 2 == 0:
        even.append(numbers)
print (len(even))