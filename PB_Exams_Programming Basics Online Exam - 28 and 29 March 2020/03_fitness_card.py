available_mooney = float(input())
sex = input()
age = int(input())
sport = input()
price_card = 0
total_sum = 0
if sex == "f":
    if sport == "Gym":
        price_card = 35
    elif sport == "Boxing":
        price_card = 37
    elif sport == "Yoga":
        price_card = 42
    elif sport == "Zumba":
        price_card = 31
    elif sport == "Dances":
        price_card = 53
    elif sport == "Pilates":
        price_card = 37
if sex == "m":
    if sport == "Gym":
        price_card = 42
    elif sport == "Boxing":
        price_card = 41
    elif sport == "Yoga":
        price_card = 45
    elif sport == "Zumba":
        price_card = 34
    elif sport == "Dances":
        price_card = 51
    elif sport == "Pilates":
        price_card = 39

if age <= 19:
    total_sum = price_card * 0.80
else:
    total_sum = price_card
difference = abs(available_mooney - total_sum)
if available_mooney >= total_sum:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")