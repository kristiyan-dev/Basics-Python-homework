# скумрията- mackerel
# цацата- sprat
# паламуд - bonito
# сафрид - safrid
# миди - mussels

mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

price_bonito = (mackerel_price * 1.60) * bonito_kg
price_safrid = (sprat_price * 1.80) * safrid_kg
price_mussels = 7.50 * mussels_kg

total_cost = price_bonito + price_safrid + price_mussels

print(f'{total_cost:.2f}')



