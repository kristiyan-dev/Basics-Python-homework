annual_rent = float(input())

shoes = annual_rent * 0.60
basketball_jersey = shoes * 0.80
ball = basketball_jersey * 1 / 4
accessories = ball * 1 / 5

total_cost = shoes + basketball_jersey + ball + accessories + annual_rent

print(f"{total_cost:.2f}")