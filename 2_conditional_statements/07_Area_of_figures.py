from math import pi


geometrical_figures = input()

if geometrical_figures == "square":
    a = float(input())
    area = a * a
    print(f"{area: .3f}")

elif geometrical_figures == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")

elif geometrical_figures == "circle":
    r = float(input())
    area = pi * (r ** 2)
    print(f"{area:.3f}")

elif geometrical_figures == "triangle":
    a = float(input())
    b = float(input())
    area = 1 / 2 * a * b
    print(f"{area:.3f}")
