from typing import Callable, Any, Collection


class Jury:
    def __init__(
        self,
        fn_name: str,
        fn: Callable,
        testcases: Collection[tuple] | None = None,
        verbose: bool | str = True,
    ) -> None:
        self.name: str = fn_name
        self.jury_fn: Callable = fn
        self.testcases: Collection[tuple] | None = testcases and [*testcases]
        self.verbose: bool = verbose

    def set_testcases(self, testcases: Collection[tuple] | None) -> None:
        self.testcases = testcases and [*testcases]

    @staticmethod
    def check_verbose_target(
        current_jury,
        current_student,
        target_jury: Any | None = None,
        target_student: Any | None = None,
    ) -> bool:
        filter_jury = target_jury is None or target_jury == current_jury
        filter_student = (
            target_student is None or target_student == current_student
        )
        return filter_jury and filter_student

    def evaluate_equal(
        self,
        student_fn: Callable,
        verbose_target_jury: Any | None = None,
        verbose_target_student: Any | None = None,
    ) -> None:
        if self.testcases is None:
            raise Exception(
                "Please set testcases first before calling evaluate_equal()"
            )

        full_score = len(self.testcases)
        score = 0
        for testcase in self.testcases:
            student_ans = student_fn(*testcase)
            jury_ans = self.jury_fn(*testcase)
            if student_fn(*testcase) == self.jury_fn(*testcase):
                score += 1
                if (self.verbose == True or self.verbose == "passed") and (
                    self.check_verbose_target(
                        jury_ans,
                        student_ans,
                        verbose_target_jury,
                        verbose_target_student,
                    )
                ):
                    print(
                        f"✅ {self.name}{testcase} passed the test ({score}/{full_score}: {score/full_score*100:.2f}) | answer `{jury_ans}`"
                    )
            else:
                if (self.verbose == True or self.verbose == "failed") and (
                    self.check_verbose_target(
                        jury_ans,
                        student_ans,
                        verbose_target_jury,
                        verbose_target_student,
                    )
                ):
                    print(
                        f"❌ {self.name}{testcase} failed the test ({score}/{full_score}: {score/full_score*100:.2f}%) | expected `{jury_ans}`, got `{student_ans}`"
                    )
        print()
        print(
            f"📋 Total score: {score}/{full_score}: {score/full_score*100:.2f}%"
        )
