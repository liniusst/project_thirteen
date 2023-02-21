from mod.calculator import prod_and_div
from mod.mod_add_string import add_name_ending
from mod.mod_add_to_list import add_to_list
from mod.mod_add_len import get_name_len
from typing import Tuple, List, Union

# Create a simple calculus program as a script and as module.
# def add_and_sub(number_one: int, number_two: int) -> Tuple[int, int]:
#     add = number_one + number_two
#     sub = number_one - number_two
#     return add, sub

# result_add_sub = add_and_sub(5, 10)
# print(f'add and sub: {result_add_sub}')

# result_prod_div = prod_and_div(5, 10)
# print(f'prod and div: {result_prod_div}')

# Create a program with 3 different modules:
# * first, to do basic tasks with strings
# * second, basic tasks with lists.
# * third, basic tasks with numbers
# Import them as modules to the main.py module and show calculations.

def all_mods(name: str) -> List[str]:
    name = input('Enter your name: ')
    new_name = add_name_ending(name)
    appended_list = add_to_list(new_name)
    name_len = get_name_len(appended_list)
    appended_list.append(name_len)
    return print(f' Your new name should be {new_name} with {name_len} lenght. List: {appended_list}')

all_mods('')
