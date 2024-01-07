number_of_pens = int(input())
number_of_markers = int(input())
liters_of_dergents = int(input())
discount_oercent = int(input())
price_pens = 5.80
price_for_markers = 7.20
price_per_detergent = 1.20

needed_sum = number_of_pens * price_pens \
             + number_of_markers * price_for_markers \
             + liters_of_dergents * price_per_detergent
total_sum = needed_sum - needed_sum * discount_oercent / 100

print(total_sum)