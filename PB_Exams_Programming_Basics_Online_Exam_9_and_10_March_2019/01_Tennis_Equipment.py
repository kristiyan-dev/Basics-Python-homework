import math

price_tennis_racket = float(input())
number_of_racket = int(input())
number_of_shoes = int(input())

price_of_shoes = price_tennis_racket * 1 / 6
cost_of_racket = number_of_racket * price_tennis_racket
cost_of_shoes = number_of_shoes * price_of_shoes
other_equipment = 0.20 * (cost_of_shoes + cost_of_racket)

total_cost = cost_of_shoes + cost_of_racket + other_equipment

djokovic_cost = total_cost * 1 / 8
sponsor_cost = total_cost * 7 / 8

print(f"Price to be paid by Djokovic {math.floor(djokovic_cost)}")
print(f"Price to be paid by sponsors {math.ceil(sponsor_cost)}")
