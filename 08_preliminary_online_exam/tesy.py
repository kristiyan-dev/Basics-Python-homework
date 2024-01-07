k = int(input())
l = int(input())
m = int(input())
n = int(input())
valid = False

for first_digit_first_number in range(k, 8 + 1):
    for second_digit_first_number in range(9, l + 1, -1):
        for first_digit_second_number in range(m, 8 + 1):
            for second_digit_second_number in range(9, n + 1, -1):
                if first_digit_first_number % 2 == 0 \
                        and first_digit_second_number % 2 == 0 \
                        and second_digit_first_number % 2 != 0 \
                        and second_digit_second_number % 2 != 0:
                        # and first_digit_first_number != first_digit_second_number \
                        # and second_digit_first_number != second_digit_second_number:
                    valid = True
                    if first_digit_first_number == first_digit_second_number \
                            and second_digit_first_number == second_digit_second_number:
                        print("Cannot change the same player.")
                    else:
                        print(f"{first_digit_first_number}{second_digit_first_number} - {first_digit_second_number}{second_digit_second_number}")