"""
This module is written for evaluating functions that require students to use `print()`
as output instead of returning a value.

You may find an example of how to use this module in the `if __name__ == "__main__":` section.
"""

import builtins
import jury._print_override_buffer as pseudo_buffers


def print_override(*args, sep=" ", end="\n") -> None:
    pseudo_buffers.current_buffer.append(sep.join(map(str, args)) + end)


def toggle_buffer() -> None:
    if pseudo_buffers.current_buffer is pseudo_buffers.student_buffer:
        pseudo_buffers.current_buffer = pseudo_buffers.jury_buffer
    else:
        pseudo_buffers.current_buffer = pseudo_buffers.student_buffer


def unset():
    builtins.print = pseudo_buffers.builtins_print


def clean_output(text) -> str:
    return "\n".join(map(lambda x: x.rstrip(), text.split("\n"))).rstrip()


def retrieve_prints() -> (str, str):
    student_print = clean_output("".join(pseudo_buffers.student_buffer))
    jury_print = clean_output("".join(pseudo_buffers.jury_buffer))
    return student_print, jury_print


def setup() -> None:
    # override Python built-in `print()` to return a string instead of
    # passing the string to standard output
    builtins_print = print
    builtins.print = print_override


if __name__ == "__main__":
    from jury.test_print_override import caller_jury, caller_student

    setup()  # replace `print()` with our fake one
    caller_student()  # call the student's function that print something into student's buffer
    toggle_buffer()  # switch the buffer to print strings to jury's
    caller_jury()  # call the student's function that print something into student's buffer
    unset()  # restore `print()` to Python built-in's

    # read cleaned outputs from both student and jury
    student, jury = retrieve_prints()

    # we can now use built-in print as usual
    # because we call `setup()` and `unset()` to solve the problem
    print("==== Student said ====", student, sep="\n")
    print("==== Jury said ====", jury, sep="\n")

    # notice in the output that the last empty line is removed (without setting parameter `end` otherwise),
    # and there are no whitespaces at the end of every line.
    # this is because we use `clean_output()` to remove those noises so that it should not
    # be a problem for evaluation.
