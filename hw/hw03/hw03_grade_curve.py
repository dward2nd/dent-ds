def evaluate_with_curve(score: float, mu: float, sigma: float) -> str:
    if score < mu - 1.5 * sigma:
        return "F"
    elif score < mu - 1.0 * sigma:
        return "D"
    elif score < mu - 0.5 * sigma:
        return "D+"
    elif score < mu:
        return "C"
    elif score < mu + 0.5 * sigma:
        return "C+"
    elif score < mu + 1.0 * sigma:
        return "B"
    elif score < mu + 1.5 * sigma:
        return "B+"

    return "A"


if __name__ == "__main__":
    args = [float(x) for x in input().split()]
    print(evaluate_with_curve(*args))
