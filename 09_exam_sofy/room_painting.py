import math

number_of_cans_of_paint = int(input())
number_of_wallpaper_rolls = int(input())
price_of_one_gloves = float(input())
price_for_one_brush = float(input())

prise_paint = number_of_cans_of_paint * 21.50
price_wallpaper = number_of_wallpaper_rolls * 5.20
needed_gloves = math.ceil(number_of_wallpaper_rolls * 0.35)
price_gloves = price_of_one_gloves * needed_gloves
needed_brush = math.floor(number_of_cans_of_paint * 0.48)
price_brush = price_for_one_brush * needed_brush

total_cost = prise_paint + price_wallpaper + price_gloves + price_brush

delivery_cost = f'{total_cost * 1/15:.2f}'

print(f"This delivery will cost {delivery_cost} lv.")
