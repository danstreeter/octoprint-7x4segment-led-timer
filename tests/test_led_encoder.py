# System Imports
import unittest

# Framework / Library Imports

# Application Imports
from src.led_encoder import (
    chars_to_binary,
    encode,
    custom_char
)

# Local Imports

class TestLedEncoder(unittest.TestCase):

    def _bin_to_dec(self, binary):
        return int('0' + ''.join(reversed(binary)), base=2)

    def test_chars_to_binary(self):
        """
        Tests that the chars_to_binary method returns the expected value
        """
        # self.assertEqual(encode('aaaaaaa'), '0000001')
        test_data = [
            ('aaaaaaa', '0000000'),
            ('aAaaaaa', '0100000'),
            ('aaAaaaa', '0010000'),
            ('aaaAaaa', '0001000'),
            ('aaaaAaa', '0000100'),
            ('aaaaaAa', '0000010'),
            ('aaaaaaA', '0000001'),
            ('aaaaaAA', '0000011'),
            ('aaaaAAA', '0000111'),
            ('aaaAAAA', '0001111'),
            ('aaAAAAA', '0011111'),
            ('aAAAAAA', '0111111'),
            ('AAAAAAA', '1111111'),
        ]
        for test in test_data:
            self.assertEqual(encode(test[0]), self._bin_to_dec(test[1]))

    def test_led_encoder_custom_char(self):
        """
        """
        # TODO - This needs to be done manually as the LED binary
        # does not correlate directly to ascii values.
        self.assertEqual(custom_char('b'),124)