def shout_solution1(text):
    """Use f-string to get the result"""
    n = len(text)
    sharps = "#" * (n + 6)  # Don't Repeat Yourself
    return f"""{sharps}
## {text} ##
{sharps}"""


def shout_solution2(text):
    """Use + to concatenate (combine) strings with newlines (\\n)"""
    sharps = "#" * (len(text) + 6)
    mid = f"## {text} ##"
    return sharps + "\n" + mid + "\n" + sharps


def shout_solution3(text):
    """Use .join() method to concatenate (cover this later)"""
    sharps = "#" * (len(text) + 6)
    return "\n".join([sharps, f"## {text} ##", sharps])


if __name__ == "__main__":
    text = input()
    print("solution 1:", shout_solution1(text), sep="\n", end="\n\n")
    print("solution 2:", shout_solution2(text), sep="\n", end="\n\n")
    print("solution 3:", shout_solution3(text), sep="\n", end="\n\n")
