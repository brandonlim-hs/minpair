from . import arpabet
from .corpus import require as corpus_require
from collections import defaultdict
from nltk.corpus import brown
from nltk.corpus import cmudict
from nltk.corpus import words
import re


def vowel_minpair(vowels: list, pos: list = []):
    """Find words that differ in only the vowel phonological element, for the given vowel arpabets.

    For example, ['bad', 'bed', 'bid'] are one of the vowel minimal pairs for ['AE', 'EH', 'IH'] vowels.

    By default, return words that adjective, noun or verb.

    Arguments:
        vowels {list} -- The given vowel arpabets. For example, ['AE', 'EH'].

    Keyword Arguments:
        pos {list} -- The list of parts of speech from universal tagset. (default: {[]}).

    Raises:
        Exception: If less than two unique vowel arpabets is given.
        Exception: If non-vowel arpabet is given.

    Returns:
        list -- A list of dictionaries. Each dictionary maps vowels to words.
    """
    vowels = {arpabet.destress(vowel.upper()) for vowel in vowels}
    if len(vowels) < 2:
        raise Exception('At least a pair of unique vowels required.')
    if any(not arpabet.is_vowel(vowel) for vowel in vowels):
        raise Exception('Only vowels are accepted.')
    corpus_require(['brown', 'cmudict', 'universal_tagset', 'words'])
    possible_pairs = defaultdict(lambda: {})
    vowels_regex = re.compile(r'^(?:%s)' % '|'.join(vowels))
    pos = pos or ['ADJ', 'NOUN', 'VERB']
    tagged_words = {word
                    for word, tag in brown.tagged_words(tagset='universal')
                    if tag in pos}
    english_words = set(words.words()).intersection(tagged_words)
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
    return [matched_vowel
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
