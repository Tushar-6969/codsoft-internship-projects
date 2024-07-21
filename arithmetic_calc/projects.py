def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! That dont seem like a number. Please try again.")

def choose_operation():
    operations = ['+', '-', '*', '/', '**', '%']
    while True:
        operation = input("What operation u like to perform? (+, -, *, /, **, %): ").strip()
        if operation in operations:
            return operation
        else:
            print("Hmm, that dont look right. Please choose from +, -, *, /, **, %.")

def perform_calculation(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        if second_number == 0:
            return "Error: Division by zero not allowed."
        return first_number / second_number
    elif operation == '**':
        return first_number ** second_number
    elif operation == '%':
        if second_number == 0:
            return "Error: Division by zero not allowed."
        return first_number % second_number
    else:
        return "Invalid operation."

def main():
    print("Welcome to the Friendly Arithmatic Calculator!")

    while True:
        first_number = get_number("Plz enter the first number: ")
        second_number = get_number("Plz enter the second number: ")
        operation = choose_operation()
        result = perform_calculation(first_number, second_number, operation)
        
        print(f"The result of {first_number} {operation} {second_number} is: {result}")
        
        another_calculation = input("Would u like to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            break

    print("Thank you for using the Friendly Arithmatic Calculator! Have a great day!")

if __name__ == "__main__":
    main()
