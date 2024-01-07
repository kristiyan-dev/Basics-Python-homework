name_of_actor = input()
academy_points = float(input())
jury = int(input())

total_points = 0
actor_points = 0
total_sum = 0
for _ in range(1, jury + 1):
    evaluator_name = input()
    evaluator_points = float(input())
    actor_points = len(evaluator_name) * evaluator_points / 2
    total_points += actor_points
    total_sum = total_points + academy_points
    if total_sum >= 1250.5:
        break


difference = abs(total_sum - 1250.5)

if total_sum >= 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_sum:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")