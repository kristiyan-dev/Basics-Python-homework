import math

one_gpu = int(input())
one_transition = int(input())
price_for_current_consumed = float(input())
profit_one_gpu = float(input())

price_gpu = one_gpu * 13
price_transition = one_transition * 13
total_money_spend = price_gpu + price_transition + 1000
profit_gpu_per_day = profit_one_gpu - price_for_current_consumed
total_profit_gpu =  profit_gpu_per_day * 13

needed_day = total_money_spend / total_profit_gpu

print(total_money_spend)
print(math.ceil(needed_day))
      