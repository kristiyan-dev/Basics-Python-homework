budget = float(input())
season = input()
destination = ""
accommodation = ""
output_price = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        output_price = budget * 0.30
    elif season == "winter":
        accommodation = "Hotel"
        output_price = budget * 0.70


elif 1000 >= budget:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        output_price = budget * 0.40
    elif season == "winter":
        accommodation = "Hotel"
        output_price = budget * 0.80

elif budget > 1000:
    destination = "Europe"
    if season == "summer":
        accommodation = "Hotel"
        output_price = budget * 0.90
    elif season == "winter":
        accommodation = "Hotel"
        output_price = budget * 0.90


print(f"Somewhere in {destination}" )
print(f"{accommodation} - {output_price:.2f}")