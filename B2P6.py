# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]
result = numbers[0] - sum(numbers[1:])
print(result)
