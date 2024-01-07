minutes_checkpoint = int(input())
seconds_checkpoint = int(input())
long_in_mt = float(input())
seconds_for_100_mt = int(input())

total_seconds = minutes_checkpoint * 60 + seconds_checkpoint
time_delay = long_in_mt / 120
total_time_delay = time_delay * 2.5
total_time = (long_in_mt / 100) * seconds_for_100_mt - total_time_delay

diff = abs(total_time - total_seconds)
if total_time <= total_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")