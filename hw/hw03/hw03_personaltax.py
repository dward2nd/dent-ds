import math


def personal_income_tax(
    income: float, witholding: float, deductable: float
) -> float:
    income -= deductable
    tax = 0

    if income > 150_000:
        tax += min(income - 150_000, 150_000) * 0.05

    if income > 300_000:
        tax += min(income - 300_000, 200_000) * 0.1

    if income > 500_000:
        tax += min(income - 500_000, 250_000) * 0.15

    if income > 750_000:
        tax += min(income - 750_000, 250_000) * 0.2

    if income > 1_000_000:
        tax += min(income - 1_000_000, 1_000_000) * 0.25

    if income > 2_000_000:
        tax += min(income - 2_000_000, 3_000_000) * 0.3

    if income > 5_000_000:
        tax += (income - 5_000_000) * 0.35

    return tax - witholding


# alternatively
def tax_bracket(
    income: float, begin: float, end: float, ratio: float
) -> float:
    return min(end - begin, max(0, income - begin)) * ratio


def personal_income_tax_alt(
    income: float, witholding: float, deductable: float
) -> float:
    income -= deductable

    return (
        tax_bracket(income, 150_000, 300_000, 0.05)
        + tax_bracket(income, 300_000, 500_000, 0.1)
        + tax_bracket(income, 500_000, 750_000, 0.15)
        + tax_bracket(income, 750_000, 1_000_000, 0.2)
        + tax_bracket(income, 1_000_000, 2_000_000, 0.25)
        + tax_bracket(income, 2_000_000, 5_000_000, 0.3)
        + tax_bracket(income, 5_000_000, math.inf, 0.35)
        # math.inf is infinity implementation from IEEE-754,
        # representing infinity number
    ) - witholding


if __name__ == "__main__":
    args = [float(x) for x in input().split()]
    print(personal_income_tax(*args))
    print(personal_income_tax_alt(*args))
