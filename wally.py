import re
import inspect

input_list = ['Wenda', 'Wizard Whitebeard', 'Wally', 'Woof', 'Odlaw', 'The Wally Watchers']

input_str = ", ".join(input_list)

print(input_str)

match_iter = re.finditer(r"Wally", input_str)

print(list(match_iter))

print([elm[0] for elm in inspect.getmembers(match_iter)])

print(match_iter)
