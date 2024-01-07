from sys import maxsize
max_number = -maxsize

while True:
    command = input()
    if command == "Stop":
        break
    numbers = int(command)
    if numbers > max_number:
        max_number = numbers
print(max_number)
