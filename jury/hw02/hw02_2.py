from bbhw.hw02.hw02_2 import t as student_fn
from hw.hw02.hw02_2 import to_timestamp as jury_fn
from jury.template import Jury


def main() -> None:
    jury = Jury("to_timestamp", jury_fn)
    jury.set_testcases(map(lambda x: (x,), range(360000)))
    jury.evaluate_equal(student_fn)


if __name__ == "__main__":
    main()
