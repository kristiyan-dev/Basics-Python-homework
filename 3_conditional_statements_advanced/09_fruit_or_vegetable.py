name_product = input()
output = ""

if name_product == "banana" \
        or name_product == "apple" \
        or name_product == "kiwi" \
        or name_product == "cherry" \
        or name_product == "lemon" \
        or name_product == "grapes":
    output = "fruit"

elif name_product == "tomato" or name_product == "cucumber" or name_product == "pepper" or name_product == "carrot":
    output = "vegetable"

else:
    output = "unknown"

print(output)