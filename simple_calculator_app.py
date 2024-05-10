# Define function of each operation
def add(first_number, second_number):
    return int(first_number + second_number)


def subtract(first_number, second_number):
    return int(first_number - second_number)


def multiply(first_number, second_number):
    return int(first_number * second_number)


def divide(first_number, second_number):
    try:
        return int(first_number / second_number)
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


def calculator():
    while True:
        print("\n\033[3mSimple App Calculator")
        print("\n\033[1;95mChoose an operation:")
        print("\033[0;36m1. Addition")
        print("\033[0;36m2. Subtraction")
        print("\033[0;36m3. Multiplication")
        print("\033[0;36m4. Division")
        
# Define calculator function
# Loop until user opts to exit