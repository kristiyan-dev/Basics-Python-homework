number_of_location = int(input())

gold_per_day = 0
total_avg_gold = 0
total_sum = 0
for locations in range(1, number_of_location + 1):
    expected_average = int(input())
    number_of_day_per_digging = int(input())
    total_avg_gold += expected_average
    gold_per_day = 0
    total_avg_gold = 0
    total_sum = 0
    for i in range(1, number_of_day_per_digging + 1):
        gold_production_per_day = float(input())
        gold_per_day += gold_production_per_day
        total_sum = gold_per_day / number_of_day_per_digging
    diff = abs(expected_average - total_sum)

    if total_sum >= expected_average:
        print(f"Good job! Average gold per day: {total_sum:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")
