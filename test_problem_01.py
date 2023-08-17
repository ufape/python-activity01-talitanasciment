# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Description:

import os.path
import sys

from problem_01 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_01():
    if not os.path.exists("problem_01.py"):
        sys.exit("Error: problem_01.py not found")

    expected_output = [
        "Hello, World!"
    ]

    set_keyboard_input([])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
