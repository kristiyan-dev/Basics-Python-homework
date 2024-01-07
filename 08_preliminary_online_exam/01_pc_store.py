price_cpu_usd = float(input())
price_gpu_usd = float(input())
price_ram_per_qty_usd = float(input())
number_ram = int(input())
percent_discount = float(input())

final_price_cpu = price_cpu_usd * 1.57
final_price_gpu = price_gpu_usd * 1.57
final_price_ram = (price_ram_per_qty_usd * 1.57) * number_ram

discount_cpu = final_price_cpu * percent_discount
discount_gpu = final_price_gpu * percent_discount
price_discount_cpu = final_price_cpu - discount_cpu
price_discount_gpu =  final_price_gpu - discount_gpu

total_sum = final_price_ram + price_discount_cpu + price_discount_gpu

print(f"Money needed - {total_sum:.2f} leva.")
