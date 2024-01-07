products = input()
city = input()
qty = float(input())
price = 0

if city == "Sofia":
    if products == "coffee":
        price = 0.50
    elif products == "water":
        price = 0.80
    elif products == "beer":
        price = 1.20
    elif products == "sweets":
        price = 1.45
    elif products == "peanuts":
        price = 1.60
if city == "Plovdiv":
    if products == "coffee":
        price = 0.40
    elif products == "water":
        price = 0.70
    elif products == "beer":
        price = 1.15
    elif products == "sweets":
        price = 1.30
    elif products == "peanuts":
        price = 1.50
if city == "Varna":
    if products == "coffee":
        price = 0.45
    elif products == "water":
        price = 0.70
    elif products == "beer":
        price = 1.10
    elif products == "sweets":
        price = 1.35
    elif products == "peanuts":
        price = 1.55
total = price * qty
print(total)