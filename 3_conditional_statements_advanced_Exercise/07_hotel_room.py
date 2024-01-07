month = input()
number_of_night = int(input())

price_for_studio = 0
price_for_apartments = 0
total_price_studio = 0
total_price_apartments = 0

if month == "May" or month == "October":
    price_for_studio = 50
    price_for_apartments = 65
    if 7 < number_of_night <= 14:
        price_for_studio *= 0.95
    elif number_of_night > 14:
        price_for_studio *= 0.70
        price_for_apartments *= 0.90
total_price_studio = price_for_studio * number_of_night
total_price_apartments = price_for_apartments * number_of_night


if month == "June" or month == "September":
    price_for_studio = 75.20
    price_for_apartments = 68.70
    if number_of_night > 14:
        price_for_studio *= 0.80
        price_for_apartments *= 0.90
total_price_studio = price_for_studio * number_of_night
total_price_apartments = price_for_apartments * number_of_night

if month == "July" or month == "August":
    price_for_studio = 76
    price_for_apartments = 77
    if number_of_night > 14:
        price_for_apartments *= 0.90
total_price_studio = price_for_studio * number_of_night
total_price_apartments = price_for_apartments * number_of_night

print(f"Apartment: {total_price_apartments:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
