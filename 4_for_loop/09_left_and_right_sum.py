n = int(input())

total_sum_first_number = 0
total_sum_second_number = 0
for _ in range(n):
    first_number = int(input())
    total_sum_first_number += first_number
for _ in range(n):
    second_number = int(input())
    total_sum_second_number += second_number


difference = abs(total_sum_first_number - total_sum_second_number)

if total_sum_first_number == total_sum_second_number:
    print(f"Yes, sum = {total_sum_first_number}")
else:
    print(f"No, diff = {difference}")
