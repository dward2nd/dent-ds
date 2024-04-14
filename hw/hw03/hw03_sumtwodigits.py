def ensure_int(n: int | str) -> int:
    """Assuming that `n` can be only either `int` or `str`"""
    if isinstance(n, str):
        return ord(n) - ord("0")
    return n


def sum_two_digits(a: int | str, b: int | str) -> int:
    a = ensure_int(a)
    b = ensure_int(b)

    return a + b
