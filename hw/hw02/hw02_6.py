def animal_year(n):
    return (n - 4) % 12 + 1


if __name__ == "__main__":
    n = int(input())
    print(animal_year(n))
