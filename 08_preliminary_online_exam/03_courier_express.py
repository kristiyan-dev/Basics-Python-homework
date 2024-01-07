weight = float(input())
type_of_service = input()
distance = int(input())
price = 0
discount = 0
total_cost = 0

if type_of_service == "standard":
    if weight < 1:
        price = 3
    elif 1 < weight < 10:
        price = 5
    elif 10 <= weight < 40:
        price = 10
    elif 40 <= weight < 90:
        price = 15
    elif 90 <= weight < 150:
        price = 20
elif type_of_service == "express":
    if weight < 1:
        price = 3
        discount = price * 0.8 * weight * distance / 100
    elif 1 < weight < 10:
        price = 5
        discount = price * 0.4 * weight * distance / 100
    elif 10 <= weight < 40:
        price = 10
        discount = price * 0.05 * weight * distance / 100
    elif 40 <= weight < 90:
        price = 15
        discount = price * 0.02 * weight * distance / 100
    elif 90 <= weight < 150:
        price = 20
        discount = price * 0.01 * weight * distance / 100

if type_of_service == "standard":
    total_cost = price / 100 * distance
elif type_of_service == "express":
    total_cost = discount + (price / 100 * distance)

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_cost:.2f} lv.")