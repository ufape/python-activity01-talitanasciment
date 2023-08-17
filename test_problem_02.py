# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 2
# Description:

import os.path
import sys

from problem_02 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_02():
    if not os.path.exists("problem_02.py"):
        sys.exit("Error: problem_02.py not found")

    expected_output = [
        "Digite o valor de A: ",
        "Digite o valor de B: ",
        "Soma = 19"
    ]

    set_keyboard_input([10, 9])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
