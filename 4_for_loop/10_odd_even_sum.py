n = int(input())
odd = 0
even = 0
for i in range(n):
    current_number = int(input())
    if i % 2 == 0:
        even += current_number
    else:
        odd += current_number


difference = abs(odd - even)
if odd == even:
    print("Yes")
    print(f"Sum = {odd}")

else:
    print("No")
    print(f"Diff = {difference}")
