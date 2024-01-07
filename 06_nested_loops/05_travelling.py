destination = input()

while destination != "End":
    budget = float(input())
    current_money = 0
    while current_money < budget:
        savings = float(input())
        current_money += savings
    print(f"Going to {destination}!")
    destination = input()

