def animal_year(n):
    return (n - 4) % 12 + 1


def element_year(n):
    return (n // 2 - 3) % 6 + 1


def print_full_zodiac_year(n):
    print("animal:", animal_year(n))
    print("element:", element_year(n))


if __name__ == "__main__":
    n = int(input())
    print_full_zodiac_year(n)
