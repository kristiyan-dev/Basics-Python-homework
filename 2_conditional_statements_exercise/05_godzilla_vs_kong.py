budget = float(input())
number_of_statist = int(input())
cost_for_dress = float(input())

decors_film = budget * 0.10

total_cost_dress = number_of_statist * cost_for_dress
if number_of_statist > 150:
    total_cost_dress *= 0.90

total_sum = decors_film + total_cost_dress

difference = abs(budget - total_sum)

if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")

elif total_sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
