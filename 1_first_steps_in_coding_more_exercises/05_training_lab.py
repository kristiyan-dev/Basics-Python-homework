length_in_meters = float(input())
width_in_meters = float(input())

length_in_cm = length_in_meters * 100
height_in_cm = width_in_meters * 100

length = 70
width = 120
free_space = 100
total_length_space = length_in_cm // width
total_height_space = (height_in_cm - free_space) // length

total_work_station = (total_length_space * total_height_space) - 3
print(f'{total_work_station:.0f}')
