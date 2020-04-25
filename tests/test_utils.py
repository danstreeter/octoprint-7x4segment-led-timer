# System Imports
import unittest

# Framework / Library Imports

# Application Imports
from src import utils

# Local Imports

class TestUtils(unittest.TestCase):

    def test_sec_to_mmss(self):
        """
        Tests that the sec_to_mmss function works as expected
        """
        sut = utils.sec_to_mmss
        test_data = [
            (1, "0001"),    # 1 second
            (60, "0100"),   # 1 minute
            (3600, " 100"),  # 1 hour
        ]
        for test in test_data:
            self.assertEqual(sut(test[0]), test[1])