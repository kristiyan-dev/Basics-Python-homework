height = 5364
everest = 8488
cons_days = 0
days = 0

command = input()

while command != 'End':
    metres_for_the_day = int(command)
    days += 1
    height += metres_for_the_day

    if height >= everest:
        print(f'Goal reached for {days} days!')
        exit()
    else:
        if command == 'No':
            cons_days += 1
            if cons_days > 5:
                print('Failed!')
                print(f'{height}')
                exit()
            else:
                continue
        else:
            cons_days = 0

    command = input()

else:
    print("Failed!")
    print(f'{height}')
    exit()