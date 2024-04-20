def my_abs(n: float) -> float:
    if n < 0:
        return -n
    return n


def my_abs_alt(n: float) -> float:
    match n:
        case t if t < 0:
            return -t
        case _:
            return n


if __name__ == "__main__":
    x = int(input())
    print(my_abs(x))
