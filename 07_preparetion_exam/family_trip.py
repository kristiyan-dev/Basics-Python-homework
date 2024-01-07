budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

price_for_all_period = number_of_nights * price_per_night
additional_costs = budget * (percent_additional_costs / 100)
total_costs = price_for_all_period + additional_costs

diff_costs = f'{abs(budget - total_costs):.2f}'

if total_costs <= budget:
    print(f'Ivanovi will be left with {diff_costs} leva after vacation.')
else:
    print(f'{diff_costs} leva needed.')
