height = 5364
everest = 8848
days = 1

command = input()

while command != 'END':
    metres_for_day = int(input())
    if command == "Yes":
        days += 1
        height += metres_for_day
    elif command == "No":
        height += metres_for_day

    if height >= everest:
        print(f"Goal reached for {days} days!")
        break
    elif days > 5:
        height = height - metres_for_day
        print("Failed!")
        print(f"{height}")
        break
    command = input()

if command == "END":
    print("Failed!")
    print(f"{height}")