# Create a simple calculus program as a script and as module.
import modules.mod_calculator
from modules.mod_check_user import check
from modules.mod_reverse_string import reverse
from modules.mod_trim_name import trim_name
from typing import Tuple

# def all_results(first: int, second: int) -> Tuple[int, int]:
#     add = calculator.value_plus(first, second)
#     sub = calculator.value_minus(first, second)
#     div = calculator.value_div(first, second)
#     prod = calculator.value_prod(first, second)
#     return add, sub, div, prod
# print(all_results(10, 2))

def check_reversed_name(input_name: str, char: str) -> str:
    reversed_name = reverse(input_name)
    second_char = trim_name(reversed_name)
    if char == second_char:
        check(reversed_name)
    else:
        print(f'We found admin {reversed_name}, but second char is wrong')


input_name = input('Input reversed admin name: ')
char = input('Input second name char: ')
check_reversed_name(input_name, char)