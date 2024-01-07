holiday = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minions = int(input())
truck = int(input())

puzzle_price = puzzle * 2.60
doll_price = doll * 3
bear_price = bear * 4.10
minions_price = minions * 8.20
truck_price = truck * 2

total_price_toys = puzzle_price + doll_price + bear_price + minions_price + truck_price
quantity_toys = puzzle + doll + bear + minions + truck

if quantity_toys >= 50:
    total_price_toys *= 0.75

total_price_toys *= 0.90
difference = abs(total_price_toys - holiday)
if total_price_toys >= holiday:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")


