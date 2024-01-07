dessert = input()
number_of_dessert = int(input())
data = int(input())

price_of_dessert = 0

if data <= 15:
    if dessert == "Cake":
        price_of_dessert = 24.00
    elif dessert == "Souffle":
        price_of_dessert = 6.66
    elif dessert == "Baklava":
        price_of_dessert = 12.60
if 15 < data <= 24:
    if dessert == "Cake":
        price_of_dessert = 28.70
    elif dessert == "Souffle":
        price_of_dessert = 9.80
    elif dessert == "Baklava":
        price_of_dessert = 16.98

total_sum = number_of_dessert * price_of_dessert
if data <= 22:
    if 100 < total_sum <= 200:
        total_sum = total_sum * 0.85
    elif total_sum > 200:
        total_sum = total_sum * 0.75
    else:
        total_sum = total_sum

if data <= 15:
    total_sum = total_sum * 0.90
    print(f'{total_sum:.2f}')

else:
    print(f'{total_sum:.2f}')


