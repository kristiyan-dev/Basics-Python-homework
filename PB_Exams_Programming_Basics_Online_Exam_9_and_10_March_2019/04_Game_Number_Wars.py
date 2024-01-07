first_player = input()
second_player = input()
points_first_player = 0
points_second_player = 0
winner = ""
winners_points = 0
number_wars = False
for game in range(18):
    first_card = input()
    second_card = input()
    if first_card == "End of game" or second_card == "End of game":
        print(f"{first_player} has {points_first_player} points")
        print(f"{second_player} has {points_second_player} points")
        break

    else:
        first_card = int(first_card)
        second_card = int(second_card)
        if first_card == second_card:
            number_wars = True
            continue
            # if first_card > second_card:
            #     points_first_player += first_card - second_card
            #     if number_wars:
            #         winner = first_player
            #         winners_points = points_first_player
            #         break
            # elif first_card < second_card:
            #     points_second_player += second_card - first_card

        # if first_card > second_card:
        #     points_first_player += first_card - second_card
        #     if number_wars:
        #         winner = first_player
        #         winners_points = points_first_player
        #         break
        # elif first_card < second_card:
        #     points_second_player += second_card - first_card
        #     if number_wars:
        #         winner = second_player
        #         winners_points = points_second_player
        #         break
        # elif first_card == second_card:
        #     number_wars = True
        #     continue
if number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winners_points} points")


