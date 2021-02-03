"""

Write a program that counts lines and characters in a file

Test your module interactively, using import and name qualification to fetch your exports. 

"""
from mymod import count_chars, count_lines
import unittest


class TestCounters(unittest.TestCase):
    def setUp(self):
        self.debug = True

    def test_count_lines(self):
        self.assertEqual(count_lines(file_name), 25)

    def test_count_chars(self):
        self.assertEqual(count_chars(file_name), 1524)


if __name__ == "__main__":
    file_name = "./Lesson18/task3/text.txt"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCounters)
    unittest.TextTestRunner(verbosity=2).run(suite)

