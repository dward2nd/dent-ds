# copied from hw03_grade_fixed.py
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


# copied from hw03_grade_curve.py
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


def evaluate_score(
    score: float, mu: float = 65, sigma: float = 10, use_curve: bool = False
) -> str:
    """Fun Fact: You can just

    ```python
    return evaluate_with_curve(score, mu, sigma)
    ```

    and it still works!
    """
    if use_curve:
        return evaluate_with_curve(score, mu, sigma)
    else:
        return evaluate_fixed_scale(score)
