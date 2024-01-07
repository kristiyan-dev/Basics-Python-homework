month = input()
number_hours = int(input())
number_of_people_in_group = int(input())
the_time_of_day = input()

price_per_hours = 0
if the_time_of_day == "day":
    if month == "march" or month == "april" or month == "may":
        price_per_hours = 10.50
    elif month == "june" or month == "july" or month == "august":
        price_per_hours = 12.60
if the_time_of_day == "night":
    if month == "march" or month == "april" or month == "may":
        price_per_hours = 8.40
    elif month == "june" or month == "july" or month == "august":
        price_per_hours = 10.20

if number_of_people_in_group > 4:
    price_per_hours = price_per_hours * 0.90
if number_hours >= 5:
    price_per_hours = price_per_hours * 0.50

total_cost = number_of_people_in_group * price_per_hours * number_hours

print(f"Price per person for one hour: {price_per_hours:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")
