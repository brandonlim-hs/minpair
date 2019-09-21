import unittest
from minpair import minpair


class TestArpabet(unittest.TestCase):
    def test_vowel_minpair_raises_exception_if_given_one_unique_vowel(self):
        with self.assertRaisesRegexp(Exception, 'At least a pair of unique vowels required.'):
            minpair.vowel_minpair(['AE', 'AE'])

    def test_vowel_minpair_aises_exception_if_given_consonant(self):
        with self.assertRaisesRegexp(Exception, 'Only vowels are accepted.'):
            minpair.vowel_minpair(['AE', 'B'])

    def test_vowel_minpair_returns_word_for_each_vowel(self):
        self.assertIn({'AE': 'bad', 'EH': 'bed', 'IH': 'bid'},
                      minpair.vowel_minpair(['AE', 'EH', 'IH']))
