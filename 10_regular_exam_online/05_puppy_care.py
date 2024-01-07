pay_food_in_kg = int(input())
food_in_gr = pay_food_in_kg * 1000
command = ""
total_eaten_food = 0
while command != "Adopted":
    command = input()
    if command == "Adopted":
        break
    food_per_day = int(command)
    total_eaten_food += food_per_day
    difference = abs(total_eaten_food - food_in_gr)
if total_eaten_food <= food_in_gr:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")