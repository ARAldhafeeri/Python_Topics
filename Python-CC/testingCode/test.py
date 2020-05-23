from testing import name
import unittest

class NamesTest(unittest.TestCase):
    """Tests for 'name_function.py"""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' Work ?"""
        nameme = name('janis','joplin')
        self.assertEqual(name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()


