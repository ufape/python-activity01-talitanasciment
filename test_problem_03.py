# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 3
# Description:

import os.path
import sys
from problem_03 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_03():
    if not os.path.exists("problem_03.py"):
        sys.exit("Error: problem_03.py not found")

    expected_output = [
        "Programa Simples de Pagamento\n",
        "Informe quantas horas você trabalhou: ",
        "\nContracheque",
        "\t\tHoras trabalhadas: 5",
        "\t\tValor da Hora: R$25.00",
        "\t\tSalário Bruto: R$125.00",
        "\t\tImposto: R$15.62",
        "\t\tSalário Líquido: R$109.38"
    ]

    set_keyboard_input([5])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
