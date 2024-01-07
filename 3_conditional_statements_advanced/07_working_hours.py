hours = int(input())
day = input()
output = ""

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" \
        or day == "Friday" or day == "Saturday":
    if 10 <= hours <= 18:
        output = "open"
    else:
        output = "closed"
else:
    output = "closed"
print(output)