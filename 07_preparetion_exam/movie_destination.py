budget = float(input())
destination = input()
type_of_season = input()
number_of_days = int(input())

costs = 0

if type_of_season == 'Winter':
    if destination == 'Dubai':
        costs = 45000 * number_of_days
    elif destination == 'Sofia':
        costs = 17000 * number_of_days
    elif destination == 'London':
        costs = 24000 * number_of_days


elif type_of_season == 'Summer':
    if destination == 'Dubai':
        costs = 40000 * number_of_days
    elif destination == 'Sofia':
        costs = 12500 * number_of_days
    elif destination == 'London':
        costs = 20250 * number_of_days

if destination == 'Sofia':
    costs += costs * 0.25
elif destination == 'Dubai':
    costs -= costs * 0.30

diff_costs = f'{abs(costs - budget):.2f}'

if costs > budget:
    print(f"The director needs {diff_costs} leva more!")
else:
    print(f"The budget for the movie is enough! We have {diff_costs} leva left!")
