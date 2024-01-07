day = input()
day_output = "Error"

if day == "Monday":
    day_output = "Working day"
elif day == "Tuesday":
    day_output = "Working day"
elif day == "Wednesday":
    day_output = "Working day"
elif day == "Thursday":
    day_output = "Working day"
elif day == "Friday":
    day_output = "Working day"
elif day == "Saturday":
    day_output = "Weekend"
elif day == "Sunday":
    day_output = "Weekend"

print(day_output)