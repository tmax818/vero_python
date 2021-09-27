import io
import unittest
import unittest.mock

from main import *


class TestHelloWorld(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print(self):
        self.assert_stdout('Hello World\n', 'Hello World\n')