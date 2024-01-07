first_match = input()
second_match = input()
third_match = input()

win = 0
lost = 0
drawn = 0
first_result = int(first_match[0])
first_result1 = int(first_match[2])
second_result = int(second_match[0])
second_result1 = int(second_match[2])
third_result = int(third_match[0])
third_result1 = int(third_match[2])

if first_result > first_result1:
    win += 1
elif first_result < first_result1:
    lost += 1
elif first_result == first_result1:
    drawn += 1
if second_result > second_result1:
    win += 1
elif second_result < second_result1:
    lost += 1
elif second_result == second_result1:
    drawn += 1
if third_result > third_result1:
    win += 1
elif third_result < third_result1:
    lost += 1
elif third_result == third_result1:
    drawn += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")
