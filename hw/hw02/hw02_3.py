def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


if __name__ == "__main__":
    n = int(input())
    print(f"is_even({n}) = {is_even(n)}")
    print(f"is_odd({n}) = {is_odd(n)}")
