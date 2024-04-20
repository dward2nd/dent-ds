from math import log10

from bbhw.hw02.hw02_kth_digit import kth_digit as student_fn
from hw.hw02.hw02_kth_digit import kth_digit as jury_fn
from jury.template import Jury


def generate_testcases():
    constraint = range(-1000000, 1000001)
    for n in constraint:
        if n == 0:
            continue
        n_digits = int(log10(abs(n))) + 1
        for k in range(n_digits):
            yield n, k


def main():
    jury = Jury("kth_digit", jury_fn, verbose=False)
    jury.set_testcases(generate_testcases())
    jury.evaluate_equal(student_fn)


if __name__ == "__main__":
    main()
