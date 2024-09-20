# a function taking in two parameters a and b and returning the sum

def add_numbers(a, b):
    sum = a + b
    return sum

# getting the numbers as inputs from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# display the sum of the two numbers
print(f'The sum of the numbers {a} and {b} is: {add_numbers(a, b)}')
