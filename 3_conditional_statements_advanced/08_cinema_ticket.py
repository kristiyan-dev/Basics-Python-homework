day = input()
price_output = ""

if day == "Monday" or day == "Tuesday" or day == "Friday":
    price_output = 12
elif day == "Wednesday" or day == "Thursday":
    price_output = 14
elif day == "Saturday" or day == "Sunday":
    price_output = 16

print(price_output)
