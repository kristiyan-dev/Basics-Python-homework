# Wrapping paper - BGN 5.80
# Cloth - BGN 7.20
# Glue - BGN 1.20

number_of_wrapping_paper = int(input())
number_of_cloth = int(input())
qty_glue = float(input())
discount = int(input())

total_wrapping_paper = number_of_wrapping_paper * 5.80
total_cloth = number_of_cloth * 7.20
total_glue = qty_glue * 1.20

total_sum = total_wrapping_paper + total_cloth + total_glue


discount_total = (total_sum * discount) / 100
final_cost = total_sum - discount_total
print(f"{final_cost:.3f}")


