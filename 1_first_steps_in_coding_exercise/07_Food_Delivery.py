chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegetarian_menu = 8.15
delivery = 2.50

total_chicken_menu = chicken_menu * price_chicken_menu
total_fish_menu = fish_menu * price_fish_menu
total_vegetarian_menu = vegetarian_menu * price_vegetarian_menu
total_menu = total_chicken_menu + total_fish_menu + total_vegetarian_menu
desert = total_menu * 0.20

total_cost = total_menu + desert + delivery

print(total_cost)
