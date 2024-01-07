record_in_seconds = float(input())
distance_of_meters = float(input())
time_in_seconds = float(input())

total_time = distance_of_meters * time_in_seconds
slow_time = distance_of_meters // 15 * 12.5


finish_time = total_time + slow_time
difference = abs(finish_time - record_in_seconds)
if finish_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {finish_time:.2f} seconds.")

else:
    print(f" No, he failed! He was {difference:.2f} seconds slower.")
