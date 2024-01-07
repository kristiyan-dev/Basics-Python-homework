number_of_students = int(input())
top_students = 0
excellent = 0
good = 0
fail = 0
total_grade = 0

for i in range(1, number_of_students + 1):
    students_grade = float(input())
    if 5 <= students_grade:
        top_students += 1
        total_grade += students_grade
    elif 4.00 <= students_grade < 4.99:
        excellent += 1
        total_grade += students_grade
    elif 3.00 <= students_grade < 3.99:
        good += 1
        total_grade += students_grade
    elif 3 > students_grade:
        fail += 1
        total_grade += students_grade
avg = total_grade / number_of_students

percent_top = (top_students / number_of_students) * 100
percent_between_4_5 = (excellent / number_of_students) * 100
percent_between_3_4 = (good / number_of_students) * 100
percent_fail = (fail / number_of_students) * 100

print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_3_4:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {avg:.2f}")
