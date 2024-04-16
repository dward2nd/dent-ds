def kth_digit(number, k):
    return abs(number) // 10**k % 10


if __name__ == "__main__":
    number = int(input())
    k = int(input())
    print(kth_digit(number, k))
