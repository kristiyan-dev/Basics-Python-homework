time_to_walking = int(input())
number_of_walks = int(input())
calories = int(input())

total_walking = number_of_walks * time_to_walking
burn_calories = total_walking * 5

if burn_calories >= calories * 0.50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")