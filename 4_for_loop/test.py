from sys import maxsize

n = int(input())
total_sum = 0

max_number = - maxsize

for i in range(n):
    numbers = int(input())
    total_sum += numbers
    if numbers > max_number:
        max_number = numbers
if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
