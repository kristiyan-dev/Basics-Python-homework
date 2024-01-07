type_flowers = input()
number_of_flowers = int(input())
budget = int(input())
price_per_flowers = 0

if type_flowers == "Roses":
    price_per_flowers = 5
    if number_of_flowers > 80:
        price_per_flowers = price_per_flowers * 0.9

elif type_flowers == "Dahlias":
    price_per_flowers = 3.80
    if number_of_flowers > 90:
        price_per_flowers = price_per_flowers * 0.85

elif type_flowers == "Tulips":
    price_per_flowers = 2.80
    if number_of_flowers > 80:
        price_per_flowers = price_per_flowers * 0.85

elif type_flowers == "Narcissus":
    price_per_flowers = 3
    if number_of_flowers < 120:
        price_per_flowers = price_per_flowers * 1.15

elif type_flowers == "Gladiolus":
    price_per_flowers = 2.50
    if number_of_flowers < 80:
        price_per_flowers = price_per_flowers * 1.20 # price_per_flowers *= 1.20

total_sum = number_of_flowers * price_per_flowers


difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")