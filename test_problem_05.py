# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 5
# Description:

import os.path
import sys
from problem_05 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_05():
    if not os.path.exists("problem_05.py"):
        sys.exit("Error: problem_05.py not found")

    expected_output = [
        "Digite o valor do raio: ",
        "Volume: 14137.1550L"
    ]

    set_keyboard_input([15])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
