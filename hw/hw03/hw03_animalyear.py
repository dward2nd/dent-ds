# Copied from the last homework
def animal_year(n: int) -> int:
    return (n - 4) % 12 + 1


def animal_year_name(n: int) -> str:
    number = animal_year(n)

    if number == 1:
        return "Rat"
    elif number == 2:
        return "Ox"
    elif number == 3:
        return "Tiger"
    elif number == 4:
        return "Rabbit"
    elif number == 5:
        return "Dragon"
    elif number == 6:
        return "Snake"
    elif number == 7:
        return "Horse"
    elif number == 8:
        return "Goat"
    elif number == 9:
        return "Monkey"
    elif number == 10:
        return "Rooster"
    elif number == 11:
        return "Dog"
    else:  # the only case left is number == 12, so just use else
        return "Pig"


# This is the alternative method that we did not cover this topic yet
animal_map = [
    "",
    "Rat",
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
]


def animal_year_name_alternative(n: int) -> str:
    number = animal_year(n)
    return animal_map[number]


if __name__ == "__main__":
    x = int(input())
    print(animal_year_name(x))
