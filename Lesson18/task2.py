'''
The sys module.

The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python? If so, does it affect where
Python looks for module files? Run some interactive tests to find it out.

'''
import sys
sys.path.append('/home/mila/projects/pythoncourse')
from Lesson16.task1 import with_index


if __name__ == '__main__':
    generator = with_index([1, 2, 3])
    print(sys.path)
    print(next(generator))
    print(next(generator))
