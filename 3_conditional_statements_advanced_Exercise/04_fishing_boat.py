budget = int(input())
season = input()
fisher = int(input())

boat_rental = 0


if season == "Spring":
    boat_rental = 3000
    if 6 >= fisher:
        boat_rental *= 0.90
    elif 7 <= fisher <= 11:
        boat_rental *= 0.85
    elif fisher >= 12:
        boat_rental *= 0.75

if season == "Winter":
    boat_rental = 2600
    if 6 >= fisher:
        boat_rental *= 0.90
    elif 7 <= fisher <= 11:
        boat_rental *= 0.85
    elif fisher >= 12:
        boat_rental *= 0.75

if season == "Summer" or season == "Autumn":
    boat_rental = 4200
    if 6 >= fisher:
        boat_rental *= 0.90
    elif 7 <= fisher <= 11:
        boat_rental *= 0.85
    elif fisher >= 12:
        boat_rental *= 0.75


if fisher % 2 == 0 and not season == "Autumn":
    boat_rental *= 0.95

difference = abs(budget - boat_rental)

if budget >= boat_rental:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
