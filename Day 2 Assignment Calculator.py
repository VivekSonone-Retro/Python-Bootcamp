# Defined a Function that takes two numbers and prints their Addition
def add_two_numbers(a, b):
    # Calculate the sum of a and b
    result = a + b
    
    # Print the result using formatted string
    print(f"The sum of {a} and {b} is {result}")

# Ask the user to enter the first number
# input() returns a string, so we convert it to an integer using int()
num1 = int(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = int(input("Enter the second number: "))

# Call the function with the two numbers provided by the user
add_two_numbers(num1, num2)
