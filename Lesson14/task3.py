'''
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
'''
from functools import wraps

all_rules = {
    'type_': lambda x, a_type:
        '' if type(x) == a_type else f'Arg must be {a_type.__name__} type',
    'max_length': lambda x, max_len:
        '' if len(str(x)) <= max_len else f'Max length of arg is {max_len}',
    'contains': lambda x, contain:
        '' if all(ele in x for ele in contain) else f'Arg should contain {contain}'
}

def arg_rules(**rules):
    def decorator(func):
        @ wraps(func)
        def wrapper(*args, **kwargs):
            errors_list = []
            string = args[0]
            for key, rule in rules.items():
                validator = all_rules.get(key)
                if hasattr(validator, '__call__'):
                    error = validator(string, rule)
                    if error:
                        errors_list.append(error)
            if errors_list:
                print(string)
                print(*errors_list, sep='\n')
                print()
            return False if errors_list else func(*args, **kwargs)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

if __name__ == '__main__':
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('hsjdskdl@gmail.com') is False
    assert create_slogan('john05@gmail.ua') == 'john05@gmail.ua drinks pepsi in his brand new BMW!'
