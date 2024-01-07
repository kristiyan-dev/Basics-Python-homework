from math import ceil

name_to_film = input("")
time_to_film = int(input())
time_to_break = int(input())

time_to_eat = time_to_break / 8
rest_time = time_to_break / 4

total_time = time_to_break - time_to_eat - rest_time

difference = abs(time_to_film - total_time)
difference = ceil(difference)

if total_time > time_to_film:
    print(f"You have enough time to watch {name_to_film} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_to_film}, you need {difference} more minutes.")
