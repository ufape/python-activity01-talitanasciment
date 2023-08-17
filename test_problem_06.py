# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 6
# Description:

import os.path
import sys
from problem_06 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_06():
    if not os.path.exists("problem_06.py"):
        sys.exit("Error: problem_06.py not found")

    expected_output = [
        "Digite o valor A: ",
        "Digite o valor B: ",
        "Digite o valor C: ",
        "O maior número é: 106"
    ]

    set_keyboard_input([7, 16, 106])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
