stage_of_championship = input()
type_ticket = input()
number_ticket = int(input())
option_photo = input()
total_ticket_price = 0
price_ticket = 0
total_photo = 0

if stage_of_championship == "Quarter final":
    if type_ticket == "Standard":
        price_ticket = 55.50
    elif type_ticket == "Premium":
        price_ticket = 105.20
    elif type_ticket == "VIP":
        price_ticket = 118.90
if stage_of_championship == "Semi final":
    if type_ticket == "Standard":
        price_ticket = 75.88
    elif type_ticket == "Premium":
        price_ticket = 125.22
    elif type_ticket == "VIP":
        price_ticket = 300.40
if stage_of_championship == "Final":
    if type_ticket == "Standard":
        price_ticket = 110.10
    elif type_ticket == "Premium":
        price_ticket = 160.66
    elif type_ticket == "VIP":
        price_ticket = 400

total_photo = number_ticket * 40
total_ticket_price = number_ticket * price_ticket


if option_photo == "Y":
    if total_ticket_price > 4000:
        total_ticket_price = total_ticket_price * 0.75
    elif total_ticket_price > 2500:
        total_ticket_price = total_ticket_price * 0.90 + total_photo
    else:
        total_ticket_price = number_ticket * price_ticket + total_photo
elif option_photo == "N":
    if total_ticket_price > 4000:
        total_ticket_price = total_ticket_price * 0.75
    elif total_ticket_price > 2500:
        total_ticket_price = total_ticket_price * 0.90
    else:
        total_ticket_price = number_ticket * price_ticket
print(f"{total_ticket_price:.2f}")
