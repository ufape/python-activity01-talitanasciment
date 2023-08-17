# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 8
# Description:

import os.path
import sys
from problem_08 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_08():
    if not os.path.exists("problem_08.py"):
        sys.exit("Error: problem_08.py not found")

    expected_output = [
        "Valor (1/6): ",
        "Valor (2/6): ",
        "Valor (3/6): ",
        "Valor (4/6): ",
        "Valor (5/6): ",
        "Valor (6/6): ",
        "Detectamos 5 valores positivos."
    ]

    set_keyboard_input([7, 5, 6, -3.5, 3, 5.8])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
