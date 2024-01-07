strawberry_price = float(input())
banana_qty = float(input())
orange_qty = float(input())
raspberry_qty = float(input())
strawberry_qty = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price * 0.60
banana_price = raspberry_price * 0.20

total_sum = (raspberry_qty * raspberry_price) + (orange_qty * orange_price) + \
            (banana_qty * banana_price) + (strawberry_qty * strawberry_price)

print(f'{total_sum:.2f}')
