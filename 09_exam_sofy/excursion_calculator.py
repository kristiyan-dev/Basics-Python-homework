number_of_people = int(input())
season = input()

cost_for_people = 0

if number_of_people <= 5:
    if season == "spring":
        cost_for_people = 50.00
    elif season == "summer":
        cost_for_people = 48.50
    elif season == "autumn":
        cost_for_people = 60.00
    elif season == "winter":
        cost_for_people = 86.60
if number_of_people > 5:
    if season == "spring":
        cost_for_people = 48.00
    elif season == "summer":
        cost_for_people = 45.00
    elif season == "autumn":
        cost_for_people = 49.50
    elif season == "winter":
        cost_for_people = 85.00
total_cost = number_of_people * cost_for_people

if season == "summer":
    total_cost = total_cost * 0.85
elif season == "winter":
    total_cost = total_cost * 1.08

print(f'{total_cost:.2f} leva.')
