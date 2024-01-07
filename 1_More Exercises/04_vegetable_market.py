vegetables_price = float(input())
fruit_price = float(input())
kg_vegetables = int(input())
kg_fruit = int(input())

total_vegetable = vegetables_price * kg_vegetables
total_fruit = fruit_price * kg_fruit
total_sum = total_vegetable + total_fruit
euro = total_sum / 1.94

print(f"{euro:.2f}")

