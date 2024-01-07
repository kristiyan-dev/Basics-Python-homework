number_of_days = int(input())

liter_total = 0
degrees_total = 0

for i in range(1, number_of_days + 1):
    liter = float(input())
    liter_total += liter
    degrees = float(input())
    degrees_total += degrees * liter

average_degrees = degrees_total / liter_total

print(f"Liter: {liter_total:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 < average_degrees <= 42:
    print("Super!")
elif average_degrees > 42:
    print("Dilution with distilled water!")
