'''
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
'''
from functools import wraps


def arg_rules(**rules):
    def decorator(func):
        @ wraps(func)
        def wrapper(*args):
            all_rules = {
                'type_': lambda x, a_type: (
                    f'Arg must be {a_type.__name__} type',
                    type(x) == a_type
                ),
                'max_length': lambda x, max_len: (
                    f'Max length of arg is {max_len}',
                    len(str(x)) <= max_len
                ),
                'contains': lambda x, contain: (
                    f'Arg should contain {contain}',
                    all(ele in x for ele in contain)
                )
            }
            errors_list = []
            for key, rule in rules.items():
                if hasattr(all_rules.get(key), '__call__'):
                    (error, result) = all_rules.get(key)(args[0], rule)
                    if not result:
                        errors_list.append(error)
            if len(errors_list) >= 1:
                print(*errors_list, sep='\n')
            return not errors_list
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    print(create_slogan('john05@gmail.ua'))
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('hsjdskdl@gmail.com') is False
    assert create_slogan('john05@gmail.ua') is True
