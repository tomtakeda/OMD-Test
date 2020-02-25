import unittest
from unittest.mock import patch
from io import StringIO

from .linked_list import List


class ListTestCase(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_list_print(self, mock):
        list_ = List(1, 2, 3)
        list_.print()
        self.assertEqual(mock.getvalue(), "1\n2\n3\n")

    def test_append_scalar(self):
        list_ = List(1, 2, 3)
        list_.append(4)
        self.assertEqual(list_, List(1, 2, 3, 4))

    def test_add_another_List(self):
        list_ = List(1, 2, 3)
        tail = List(5, 6)
        list_ += tail
        self.assertEqual(list_, List(1, 2, 3, 5, 6))

    def test_shallow_copy(self):
        list_ = List(1, 2, 3)
        tail = List(5, 6)
        list_ += tail
        tail._value = 0
        self.assertEqual(list_, List(1, 2, 3, 5, 6))

    def test_add_python_list_and_List(self):
        list_ = List(1, 2, 3)
        list_ += [7, 8]
        self.assertEqual(list_, List(1, 2, 3, 7, 8))

    def test_add_empty_python_list_and_List(self):
        list_ = List(1, 2, 3)
        list_ += ()
        self.assertEqual(list_, List(1, 2, 3))

    @patch("sys.stdout", new_callable=StringIO)
    def test_iter_on_List(self, mock):
        list_ = List(1, 2, 3)
        for elem in list_:
            print(2 ** elem)
        self.assertEqual(mock.getvalue(), "2\n4\n8\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_reversed(self, mock):
        list_ = List(1, 2, 3)
        list_.print_reversed()
        self.assertEqual(mock.getvalue(), "3\n2\n1\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_on_empty_List(self, mock):
        list_ = List()
        list_.print()
        self.assertEqual(mock.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_List_with_None(self, mock):
        list_ = List(None)
        list_.print()
        self.assertEqual(mock.getvalue(), "None\n")


if __name__ == "__main__":
    unittest.main()
