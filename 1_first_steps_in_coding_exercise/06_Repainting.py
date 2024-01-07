quantity_of_nylon = int(input())
quantity_of_paint = int(input())
quantity_of_thinner = int(input())
hours = int(input())

price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00
shopping_bag = 0.40

needed_nylon = quantity_of_nylon + 2
total_price_nylon = needed_nylon * price_nylon
needed_paint = quantity_of_paint * 0.10 + quantity_of_paint
total_price_paint = needed_paint * price_paint
total_thinner = quantity_of_thinner * price_thinner
total_price_materials = total_price_nylon + total_price_paint + total_thinner + shopping_bag
cost_of_work = total_price_materials * 0.30 * hours

total_cost = total_price_materials + cost_of_work
print(total_cost)
