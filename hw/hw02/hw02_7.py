def element_year(n):
    return (n // 2 - 3) % 6 + 1


if __name__ == "__main__":
    n = int(input())
    print(element_year(n))
