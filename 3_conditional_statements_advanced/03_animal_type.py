animal = input()
output = ""
if animal == "dog":
    output = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    output = "reptile"
elif animal == "cat":
    output = "unknown"

print(output)
