def two_to_the(n):
    return 1 << n  # again, faster than 2**n


if __name__ == "__main__":
    n = int(input())
    print(two_to_the(n))
