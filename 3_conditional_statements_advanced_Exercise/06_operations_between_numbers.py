number_one = int(input())
second_number = int(input())
operation = input()
output_operation = ""
even_odd = ""

if operation == "+":
    output_operation = number_one + second_number
    if output_operation % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

elif operation == "-":
    output_operation = number_one - second_number
    if output_operation % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

elif operation == "*":
    output_operation = number_one * second_number
    if output_operation % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

elif operation == "/":
    if second_number == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        output_operation = number_one / second_number
        print(f"{number_one} / {second_number} = {output_operation:.2f}")

elif operation == "%":
    if second_number == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        output_operation = number_one % second_number
        print(f"{number_one} % {second_number} = {output_operation}")

if operation == "+" or operation == "-" or operation == "*":
    print(f"{number_one} {operation} {second_number} = {output_operation} - {even_odd}")
