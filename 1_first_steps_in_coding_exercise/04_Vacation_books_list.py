number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days =int(input())

total_page_hours = (number_of_pages / pages_per_hour)
total_time = (total_page_hours / number_of_days)

print(round(total_time))
