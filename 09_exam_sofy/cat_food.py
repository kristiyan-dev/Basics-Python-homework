cat_number = int(input())

group_one = 0
group_two = 0
group_three = 0
total_eaten = 0
for i in range(cat_number):
    food_per_cat = float(input())
    if 100 <= food_per_cat < 200:
        group_one += 1
        total_eaten += food_per_cat
    elif 200 <= food_per_cat < 300:
        group_two += 1
        total_eaten += food_per_cat
    elif 300 <= food_per_cat < 400:
        group_three += 1
        total_eaten += food_per_cat

total_food = total_eaten / 1000
total_cost = total_food * 12.45

print(f'Group 1: {group_one} cats.')
print(f'Group 2: {group_two} cats.')
print(f'Group 3: {group_three} cats.')
print(f"Price for food per day: {total_cost:.2f} lv.")
