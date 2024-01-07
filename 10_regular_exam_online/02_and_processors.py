import math

number_of_cpu_make = int(input())
number_employees = int(input())
working_day = int(input())

total_hours = number_employees * working_day * 8
total_cpu_make = math.floor(total_hours / 3)

diff = abs(number_of_cpu_make - total_cpu_make)

if number_of_cpu_make <= total_cpu_make:
    total_profit = diff * 110.10
    print(f"Profit: -> {total_profit:.2f} BGN")
elif number_of_cpu_make > total_cpu_make:
    total_lost = diff * 110.10
    print(f"Losses: -> {total_lost:.2f} BGN")
