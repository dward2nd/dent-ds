def two_times(n):
    """
    Suppose n = 4 (100 in binary)
    n << k means appending k 0's onto the right of *binary* number

    n << 1: 100 0
    n << 3: 100 000

    n = 1*2^2 + 0*2^1 + 0*2^0
    n << 1 = 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0
           = 2(1*2^2 + 0*2^1 + 0*2^0)
    """
    return n << 1
    # faster than 2 * n


if __name__ == "__main__":
    n = int(input())
    print(two_times(n))
