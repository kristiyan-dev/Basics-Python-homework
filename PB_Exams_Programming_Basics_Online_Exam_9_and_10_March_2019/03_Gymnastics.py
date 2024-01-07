import math

name_country = input()
gymnastic = input()

points_of_hard = 0
points_for_play = 0
if name_country == "Russia":
    if gymnastic == "ribbon":
        points_of_hard += 9.100
        points_for_play += 9.400
    elif gymnastic == "hoop":
        points_of_hard += 9.300
        points_for_play += 9.800
    elif gymnastic == "rope":
        points_of_hard += 9.600
        points_for_play += 9.000

if name_country == "Bulgaria":
    if gymnastic == "ribbon":
        points_of_hard += 9.600
        points_for_play += 9.400
    elif gymnastic == "hoop":
        points_of_hard += 9.550
        points_for_play += 9.750
    elif gymnastic == "rope":
        points_of_hard += 9.500
        points_for_play += 9.400

if name_country == "Italy":
    if gymnastic == "ribbon":
        points_of_hard += 9.200
        points_for_play += 9.500
    elif gymnastic == "hoop":
        points_of_hard += 9.450
        points_for_play += 9.350
    elif gymnastic == "rope":
        points_of_hard += 9.700
        points_for_play += 9.150

total_points = points_of_hard + points_for_play

need_percent = 20 - total_points
percent = (need_percent / 20) * 100

print(f"The team of {name_country} get {total_points:.3f} on {gymnastic}.")
print(f"{percent:.2f}%")
