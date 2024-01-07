money_teresa = float(input())
market_money = float(input())
cost_of_teresa_of_all_period = float(input())
price_for_gift = float(input())

saved_money = money_teresa * 5
money_earned = market_money * 5
total_money_earned = saved_money + money_earned
total_money_after_cost = total_money_earned - cost_of_teresa_of_all_period

diff = abs(price_for_gift - total_money_after_cost)

if total_money_after_cost >= price_for_gift:
    print(f"Profit: {total_money_after_cost:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")