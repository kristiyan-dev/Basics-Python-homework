student = input()

grades_points = 0
years_points = 0
failed_years = 0

while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1
        if failed_years > 1:
            years_points += 1
            print(f"{student} has been excluded at {years_points} grade")
            break
        continue

    years_points += 1
    grades_points += annual_grade

    if years_points == 12:
        avg = grades_points / 12
        print(f"{student} graduated. Average grade: {avg:.2f}")
        break
