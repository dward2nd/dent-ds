def hypotenuse(a, b):
    return (a**2 + b**2) ** 0.5


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    print("%.5f" % hypotenuse(a, b))
