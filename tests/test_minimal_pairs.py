import unittest
from minimal_pairs import minimal_pairs


class TestArpabet(unittest.TestCase):
    def test_vowel_minimal_pairs_raises_exception_if_given_one_unique_vowel(self):
        with self.assertRaisesRegexp(Exception, 'At least a pair of unique vowels required.'):
            minimal_pairs.vowel_minimal_pairs(['AE', 'AE'])

    def test_vowel_minimal_pairs_aises_exception_if_given_consonant(self):
        with self.assertRaisesRegexp(Exception, 'Only vowels are accepted.'):
            minimal_pairs.vowel_minimal_pairs(['AE', 'B'])

    def test_vowel_minimal_pairs_returns_word_for_each_vowel(self):
        self.assertIn({'AE': 'bad', 'EH': 'bed', 'IH': 'bid'},
                      minimal_pairs.vowel_minimal_pairs(['AE', 'EH', 'IH']))
