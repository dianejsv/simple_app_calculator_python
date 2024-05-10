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

        choice_operation = input("\n\033[0;34mEnter choice (1/2/3/4): ")
        if choice_operation in ("1", "2", "3", "4"):
            while True:
                try:
                    first_number = float(input("Enter first number: "))
                    second_number = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            if choice_operation == "1":
                print("\n\033[31mResult: {}\033[0m".format(add(first_number, second_number)))
            elif choice_operation == '2':
                print("\n\033[31mResult: {}\033[0m".format(subtract(first_number, second_number)))
            elif choice_operation == '3':
                print("\n\033[31mResult: {}\033[0m".format(multiply(first_number, second_number)))
            elif choice_operation == '4':
                result = divide(first_number, second_number)
                if isinstance(result, str):
                    print(result)
                else:
                    print("Result: \n\033[31m{}\033[0m".format(result))
        else:
            print("Invalid choice. Please enter a valid option.")

        while True:  # This loop ensures input is either yes or no
            again = input("Do you want to try again? (yes/no): ")
# Define calculator function
# Loop until user opts to exit