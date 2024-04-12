raw_input = input().split()
a = float(raw_input[0])
b = float(raw_input[1])
c = float(raw_input[2])

x1 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)

print(f"{x1:.4f} {x2:.4f}")
