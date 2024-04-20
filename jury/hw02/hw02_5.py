from bbhw.hw02.hw02_5 import is_leap as student_fn
from hw.hw02.hw02_5 import is_leap as jury_fn
from jury.template import Jury


def main():
    jury = Jury("is_leap", jury_fn)
    jury.set_testcases(map(lambda x: (x,), range(1, 10001)))
    jury.evaluate_equal(student_fn)


if __name__ == "__main__":
    main()
