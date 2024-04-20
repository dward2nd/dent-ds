# Copied from the previous homework
def is_even(n: int) -> bool:
    return n % 2 == 0


# Copied from the previous homework
def is_odd(n: int) -> bool:
    return n % 2 == 1


def odd_or_even(n: int) -> str:
    if is_odd(n):
        return "odd"
    else:
        return "even"


if __name__ == "__main__":
    x = int(input())
    print(odd_or_even(x))
