import math

name_football_fan = input()
budget = float(input())
number_of_beer = int(input())
qty_chips = int(input())

price_beer = number_of_beer * 1.20
price_chips = (price_beer * 0.45)
total_cost_chips = math.ceil(qty_chips * price_chips)
total_cost = price_beer + total_cost_chips
diff = abs(budget - total_cost)

if total_cost <= budget:
    print(f"{name_football_fan} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_football_fan} needs {diff:.2f} more leva!")