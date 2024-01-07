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


# days = int(input())
# total_food_qty = float(input())
#
# total_cookies = 0
# total_food_eaten = 0
# total_dog_food_eaten = 0
# total_cat_food_eaten = 0
#
# for day in range(1, days + 1):
#     dog_food = int(input())
#     cat_food = int(input())
#
#     total_food_eaten += dog_food + cat_food
#
#     if day % 3 == 0:
#         total_cookies += (dog_food + cat_food) * 0.1
#
#     total_dog_food_eaten += dog_food
#     total_dog_food_eaten += cat_food
#
# percent_cookies = range(total_cookies)
#
# percent_food_eaten = (total_cat_food_eaten / total_food_qty) * 100
