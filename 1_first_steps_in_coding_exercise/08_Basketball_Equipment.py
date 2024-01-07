annual_cost = int(input())

basketball_shoes = annual_cost * 0.40
cost_shoes = annual_cost - basketball_shoes
basketball_tracksuit = cost_shoes * 0.20
cost_tracksuit = cost_shoes - basketball_tracksuit
basketball_ball = cost_tracksuit / 4
basketball_accessories = basketball_ball / 5

total_cost = annual_cost + cost_shoes + cost_tracksuit + basketball_ball + basketball_accessories

print(total_cost)