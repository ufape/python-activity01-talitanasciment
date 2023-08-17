# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 4
# Description:

import os.path
import sys
from problem_04 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_04():
    if not os.path.exists("problem_04.py"):
        sys.exit("Error: problem_04.py not found")

    expected_output = [
        "Digite o valor do raio: ",
        "Área: 12.56636m"
    ]

    set_keyboard_input([2.00])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
