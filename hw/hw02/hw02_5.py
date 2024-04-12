def is_leap(n):
    return n % 4 == 0 and n % 100 != 0 or n % 400 == 0


if __name__ == "__main__":
    n = int(input())
    print(is_leap(n))
