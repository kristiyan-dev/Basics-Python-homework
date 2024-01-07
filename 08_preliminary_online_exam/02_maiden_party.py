love_message = 0.60
wax_rose = 7.20
keychain = 3.60
caricature = 18.20
lucky_surprise = 22

needed_money = float(input())
number_love_message = int(input())
number_wax_rose = int(input())
number_keychain = int(input())
number_caricature = int(input())
number_lucky_surprise = int(input())

price_love_message = number_love_message * 0.60
price_wax_rose = number_wax_rose * 7.20
price_keychain = number_keychain * 3.60
price_caricature = number_caricature * 18.20
price_lucky_surprise = number_lucky_surprise * 22

total_price = price_love_message + price_wax_rose + price_keychain + price_caricature + price_lucky_surprise
total_qty = number_love_message + number_wax_rose + number_keychain + number_caricature + number_lucky_surprise

if total_qty >= 25:
    total_price = total_price * 0.65
total_price = total_price * 0.90

diff = abs(needed_money - total_price)
if total_price >= needed_money:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
