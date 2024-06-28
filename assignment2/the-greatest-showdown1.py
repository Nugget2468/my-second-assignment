# Ask the user to enter three numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Determine the largest number
if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

    

# Determine the smallest number
if number1 <= number2 and number1 <= number3:
    smallest = number1
elif number2 <= number1 and number2 <= number3:
    smallest = number2
else:
    smallest = number3

# Print the largest and smallest numbers
print("The smallest number is:", smallest)
print("The largest number is:", largest)