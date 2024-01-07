movie_type = input()
rows = int(input())
column = int(input())
ticket_price = 0

total_post = rows * column

if movie_type == "Premiere":
    ticket_price = total_post * 12.00
elif movie_type == "Normal":
    ticket_price = total_post * 7.50
elif movie_type == "Discount":
    ticket_price = total_post * 5.00

print(f"{ticket_price:.2f}")