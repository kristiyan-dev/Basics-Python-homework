name_product = input()
day_of_week = input()
qty = float(input())
total = 0
is_input_valid = True

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" or day_of_week == "Friday":
    if name_product == "banana":
        total = qty * 2.5
    elif name_product == "apple":
        total = qty * 1.2
    elif name_product == "orange":
        total = qty * 0.85
    elif name_product == "grapefruit":
        total = qty * 1.45
    elif name_product == "kiwi":
        total = qty * 2.70
    elif name_product == "pineapple":
        total = qty * 5.50
    elif name_product == "grapes":
        total = qty * 3.85
    else:
        is_input_valid = False
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if name_product == "banana":
        total = qty * 2.7
    elif name_product == "apple":
        total = qty * 1.25
    elif name_product == "orange":
        total = qty * 0.90
    elif name_product == "grapefruit":
        total = qty * 1.60
    elif name_product == "kiwi":
        total = qty * 3
    elif name_product == "pineapple":
        total = qty * 5.60
    elif name_product == "grapes":
        total = qty * 4.20
    else:
        is_input_valid = False
else:
    is_input_valid = False

if not is_input_valid:
    print("error")

else:
    print(f"{total:.2f}")
