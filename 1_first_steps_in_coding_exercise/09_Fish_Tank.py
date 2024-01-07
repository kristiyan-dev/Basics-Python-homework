length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = length * width * height
volume_in_litres = tank_volume * 0.001
occupied_space = volume_in_litres * percent / 100

total_water = volume_in_litres - occupied_space

print(total_water)