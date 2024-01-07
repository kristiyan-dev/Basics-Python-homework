
max_fail_points = int(input())
avg_score = 0
total_problems_solved = 0
last_problem = ""
got_too_many_bad_grades = False
fail_points = 0
current_problem = input()

while current_problem != "Enough" :
    current_grade = int(input())
    if current_grade <= 4:
        fail_points += 1
        if fail_points == max_fail_points:
            got_too_many_bad_grades = True
            break

    avg_score += current_grade
    total_problems_solved += 1
    last_problem = current_problem
    current_problem = input()

if got_too_many_bad_grades:
    print(f"You need a break, {fail_points} poor grades.")
else:
    avg_score /= total_problems_solved
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem}")