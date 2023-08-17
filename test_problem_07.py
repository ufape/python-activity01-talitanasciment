# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 7
# Description:

import os.path
import sys
from problem_07 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_07():
    if not os.path.exists("problem_07.py"):
        sys.exit("Error: problem_07.py not found")

    expected_output = [
        "Digite a distância (em km) desejada: ",
        "Levará 60 min."
    ]

    set_keyboard_input([30])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
