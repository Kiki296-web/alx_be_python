#Prompt user to input 2 numbers and operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")

    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2}.")
        else:
            print("Cannot divide by zero ")


