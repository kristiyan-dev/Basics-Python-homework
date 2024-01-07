import random


class bcolors:
    OK = "\033[92m"  # GREEN
    WARNING = "\033[93m"  # YELLOW
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


user_name = "Ivan"

user_id = "0011"
lost_money_per_month = 0
print(bcolors.OK + f"Welcome to the Slot Machine Game!\nHello {user_name}" + bcolors.RESET)

symbols = ["10", "J", "Q", "K", "A", "7"]

balance = int(input("Enter your initial balance:"))

bet = 0

while balance > 0:
    print(30 * "*")
    print("Current Balance:", balance)

    while True:
        bet = int(input("Enter your bet amount (o to exit):"))

        if bet == 0:
            break

        if bet > balance:
            print("Insufficient balance. Please a lower bet")
        else:
            break
    if bet == 0:
        break
    balance -= bet
    if user_id == "0011" and lost_money_per_month > 10000 and bet < 100:
        print(">>> Spinning the reels<<<")
        print(7, 7, 7)
        winnings = bet * 10
        balance += winnings
        print('Congratulations! You won Jackpot', winnings, 'money!"')
        lost_money_per_month = 0
        continue

    print(">>> Spinning the reels<<<")
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    print(bcolors.FAIL + reel1, reel2, reel3 + bcolors.RESET)

    if reel1 == reel2 == reel3:
        winnings = bet * 10
        balance += winnings
        print('Congratulations! You won Jackpot', winnings, 'money!"')
    elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
        winnings = bet * 2
        balance += winnings
        print(bcolors.WARNING + "Congratulations! You won", winnings, "money!" + bcolors.RESET)
    else:
        lost_money_per_month += bet
        print("Sorry! No match. Better luck next time!")
if balance == 0:
    print("Game Over! Final Balance: 0\nPlease insert money to play again!")
