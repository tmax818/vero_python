import unittest

from main import *


class TestDataTypes(unittest.TestCase):

    def test_int(self):
        self.assertIsInstance(return_int(), int)

    def test_float(self):
        self.assertIsInstance(return_float(), float)

    def test_bool(self):
        self.assertIsInstance(return_bool(), bool)

    def test_none(self):
        self.assertIsInstance(return_none(), None)