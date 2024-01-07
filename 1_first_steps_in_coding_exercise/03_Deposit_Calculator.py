deposit = float(input())
months = int(input())
annual_interest_percent = float(input())

annual_interest_percent = deposit * annual_interest_percent / 100
montly_interest = annual_interest_percent / 12
tottal_sum = deposit + months * montly_interest

print(tottal_sum)
