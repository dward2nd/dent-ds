from itertools import product

from hw.hw02.hw02_9 import is_overlapped as jury_fn
from bbhw.hw02.hw02_9 import is_overlapped as student_fn
from jury.template import Jury


def main() -> None:
    jury = Jury("is_overlapped", jury_fn)
    jury.set_testcases(
        product(
            range(-4, 5),
            range(-4, 5),
            range(1, 5),
            range(1, 5),
            range(-4, 5),
            range(-4, 5),
            range(1, 5),
            range(1, 5),
        )
    )
    jury.evaluate_equal(
        student_fn, verbose_target_jury=True, verbose_target_student=False
    )


if __name__ == "__main__":
    main()
