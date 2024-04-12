p = float(input())
r = float(input())
t = int(input())
f = int(input())

# since `r` is percentage, we need to convert to fraction first
i = r / 100

# convert every f months to n months per year
n = 12 / f

ans = p * (1 + i / n) ** (n * t / 12)
print(f"{ans:,.2f}")
