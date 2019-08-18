from collections import defaultdict
from minimal_pairs import arpabet
from nltk import download as nltk_download
from nltk.corpus import cmudict
from nltk.corpus import words
import re


def vowel_minimal_pairs(vowels: list):
    """Find words that differ in only the vowel phonological element, for the given vowel arpabets.

    For example, ['bad', 'bed', 'bid'] are one of the vowel minimal pairs for ['AE', 'EH', 'IH'] vowels.

    Arguments:
        vowels {list} -- The given vowel arpabets. For example, ['AE', 'EH'].

    Raises:
        Exception: If less than two unique vowel arpabets is given.
        Exception: If non-vowel arpabet is given.

    Returns:
        list -- A list of minimal pairs (words that differ in only vowel sound).
    """
    vowels = {arpabet.destress(vowel.upper()) for vowel in vowels}
    if len(vowels) < 2:
        raise Exception('At least a pair of unique vowels required.')
    if any(not arpabet.is_vowel(vowel) for vowel in vowels):
        raise Exception('Only vowels are accepted.')
    possible_pairs = defaultdict(lambda: {})
    vowels_regex = re.compile(r'^(?:%s)' % '|'.join(vowels))
    nltk_download('words')
    nltk_download('cmudict')
    english_words = set(words.words())
    cmudict_entries = [(word, phones)
                       for word, phones in cmudict.entries()
                       if word in english_words
                       if syllable_count(phones) == 1]
    for word, phones in cmudict_entries:
        matches = [vowels_regex.search(phone) for phone in phones]
        indices = [(i, match.group(0))
                   for i, match in enumerate(matches) if match != None]
        for index, matched_vowel in indices:
            key = tuple(phone if i != index else '.'
                        for i, phone in enumerate(phones))
            possible_pairs[key][matched_vowel] = word
    return [list(matched_vowel.values())
            for (k, matched_vowel) in possible_pairs.items()
            if set(matched_vowel) == vowels]


def syllable_count(phones: list):
    """Return the number of syllables for the given list of phones.

    For example, given phones for the word 'minimal': ['M', 'IH1', 'N', 'AH0', 'M', 'AH0', 'L'],
    should return 3 syllables.

    Arguments:
        phones {list} -- The given phones. For example, ['M', 'IH1', 'N', 'AH0', 'M', 'AH0', 'L'].

    Returns:
        int -- The number of syllables.
    """
    return sum(arpabet.has_stress(phone) for phone in phones)
