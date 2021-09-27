import unittest

from main import *


class TestDataTypes(unittest.TestCase):

    def test_true(self):
        self.assertTrue(is_true)

    def test_false(self):
        self.assertFalse(is_false, "try changing the != operator!")