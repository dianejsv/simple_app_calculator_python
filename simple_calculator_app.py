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
# Define calculator function
# Loop until user opts to exit