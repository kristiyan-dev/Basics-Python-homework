budget = float(input())
number_of_video_cards = int(input())
number_of_processor = int(input())
number_of_memory = int(input())

cost_video_cards = number_of_video_cards * 250
cost_of_processor = cost_video_cards * 0.35
cost_of_memory = cost_video_cards * 0.10

total_processor = number_of_processor * cost_of_processor
total_memory = number_of_memory * cost_of_memory

total_cost = cost_video_cards + total_processor + total_memory

if number_of_video_cards > number_of_processor:
    total_cost *= 0.85

difference = abs(total_cost - budget)

if budget >= total_cost:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")