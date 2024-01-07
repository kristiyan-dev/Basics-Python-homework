city = input()
sells = float(input())
output_commission = 0
is_input_valid = True

if city == "Sofia":
    if 0 <= sells <= 500:
        output_commission = sells * 0.05
    elif 500 < sells <= 1000:
        output_commission = sells * 0.07
    elif 1000 < sells <= 10000:
        output_commission = sells * 0.08
    elif sells > 10000:
        output_commission = sells * 0.12
    else:
        is_input_valid = False


elif city == "Varna":
    if 0 <= sells <= 500:
        output_commission = sells * 0.045
    elif 500 < sells <= 1000:
        output_commission = sells * 0.075
    elif 1000 < sells <= 10000:
        output_commission = sells * 0.10
    elif sells > 10000:
        output_commission = sells * 0.13
    else:
        is_input_valid = False


elif city == "Plovdiv":
    if 0 <= sells <= 500:
        output_commission = sells * 0.055
    elif 500 < sells <= 1000:
        output_commission = sells * 0.08
    elif 1000 < sells <= 10000:
        output_commission = sells * 0.12
    elif sells > 10000:
        output_commission = sells * 0.145
    else:
        is_input_valid = False

else:
    is_input_valid = False
if not is_input_valid:
    print("error")
else:
    print(f"{output_commission:.2f}")