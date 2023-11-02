#Calculator
#Defining funtions (add,sub,mul,div) which is (addition,subtraction,multiplication,division) and taking arguments num1,num2

def add(num1: int, num2: int):
    return num1 + num2

def sub(num1: int, num2: int):
    return num1 - num2

def mul(num1: int, num2: int):
    return num1 * num2

def div(num1: int, num2: int):
    try:
        result = num1 / num2
        return round(result, 3)
    except ZeroDivisionError:
        return "Division by zero is not allowed."

if __name__ == "__main__":
    output = 0

    while True:
        print("Methods:\n1 : +\n2 : -\n3 : *\n4 : /\n")
        num1 = int(input("Please enter 1st number: "))
        num2 = int(input("Please enter 2nd number: "))
        operation_type = int(input("Please enter method: "))

        if operation_type == 1:
            output = add(num1, num2)
        elif operation_type == 2:
            output = sub(num1, num2)
        elif operation_type == 3:
            output = mul(num1, num2)
        elif operation_type == 4:
            output = div(num1, num2)
        else:
            print("\nPlease enter a correct operator/method!\n")
            continue

        print(f"\nResult: {output}\n")
        break  # Exit the loop after displaying the result