def f(x, n):
    return (x**3 - 1) ** (1 / n)


if __name__ == "__main__":
    x = float(input())
    n = int(input())
    print("%.5f" % f(x, n))
