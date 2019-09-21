import unittest
from minpair import arpabet


class TestArpabet(unittest.TestCase):
    def test_is_vowel_returns_false_for_consonant(self):
        self.assertFalse(arpabet.is_vowel('B'))

    def test_is_vowel_returns_true_for_vowel(self):
        self.assertTrue(arpabet.is_vowel('AA'))

    def test_has_stress_returns_false_for_arpabet_without_stress(self):
        self.assertFalse(arpabet.has_stress('AA'))

    def test_has_stress_returns_true_for_arpabet_with_stress(self):
        self.assertTrue(arpabet.has_stress('AA1'))

    def test_add_stress_should_not_add_stress_for_consonant(self):
        self.assertEqual('B', arpabet.stress('B', 1))

    def test_add_stress_should_not_add_stress_for_vowel_with_stress(self):
        self.assertEqual('AA0', arpabet.stress('AA0', 1))

    def test_add_stress_should_add_stress_for_vowel_without_stress(self):
        self.assertEqual('AA1', arpabet.stress('AA', 1))

    def test_destress_should_remove_stress_for_vowel(self):
        self.assertEqual('AA', arpabet.destress('AA1'))
