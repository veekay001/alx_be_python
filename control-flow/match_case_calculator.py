number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

operation=(input("Choose the operation (+,-,*,/): "))
match operation:
    case "+":
        print("the result is: ", number1 + number2)
    case "-":
        print("the result is: ", number1 - number2)
    case "*":
        print("the result is: ", number1 * number2)
    case "/":

        if number2 != 0:
            print("the result is: ", number1 / number2)
        else:
            print("Cannot divide by zero.")

    case _:
        print("Invalid operation.")
 

    