import minpair
import pytest


def test_vowel_minpair_raises_exception_if_given_one_unique_vowel():
    with pytest.raises(Exception) as excinfo:
        minpair.vowel_minpair(['AE', 'AE'])
    assert 'At least a pair of unique vowels required.' in str(excinfo.value)


def test_vowel_minpair_raises_exception_if_given_consonant():
    with pytest.raises(Exception) as excinfo:
        minpair.vowel_minpair(['AE', 'B'])
    assert 'Only vowels are accepted.' in str(excinfo.value)


def test_vowel_minpair_returns_word_for_each_vowel():
    assert {
        'AE': 'bad',
        'EH': 'bed',
        'IH': 'bid'
    } in minpair.vowel_minpair(['AE', 'EH', 'IH'])


def test_vowel_minpair_with_pos_returns_word_for_each_vowel():
    generator = minpair.generator().pos(['VERB'])
    verb_minimal_pairs = generator.vowel_minpair(['AE', 'EH', 'IH'])
    assert {
        'AE': 'bad',
        'EH': 'bed',
        'IH': 'bid'
    } not in verb_minimal_pairs
    assert {
        'AE': 'bat',
        'EH': 'bet',
        'IH': 'bit'
    } in verb_minimal_pairs
