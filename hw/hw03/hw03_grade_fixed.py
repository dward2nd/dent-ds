def evaluate_fixed_scale(score: float) -> str:
    if score < 50:
        return "F"
    elif score < 55:
        return "D"
    elif score < 60:
        return "D+"
    elif score < 65:
        return "C"
    elif score < 70:
        return "C+"
    elif score < 75:
        return "B"
    elif score < 80:
        return "B+"

    return "A"


if __name__ == "__main__":
    score = float(input())
    print(evaluate_fixed_scale(score))
