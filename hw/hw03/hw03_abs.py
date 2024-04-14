def my_abs(n: float) -> float:
    if n < 0:
        return -n
    return n

def my_abs_alt(n: float) -> float:
    match n:
        case x if x < 0:
            return -x
        case _:
            return n


if __name__ == "__main__":
    n = int(input())
    print(my_abs(n))
