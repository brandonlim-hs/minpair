import re

VOWELS = {'AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AXR', 'AY', 'EH',
          'ER', 'EY', 'IH', 'IX', 'IY', 'OW', 'OY', 'UH', 'UW', 'UX'}


def is_vowel(arpabet: str):
    """Return true if the given arpabet is a vowel.

    Arguments:
        arpabet {str} -- The given arpabet.

    Returns:
        bool -- True if the given arpabet is a vowel.
    """
    return destress(arpabet) in VOWELS


def has_stress(arpabet: str):
    """Return true if the given arpabet end with a stress.

    Arguments:
        arpabet {str} -- The given arpabet.

    Returns:
        bool -- True if the given arpabet end with a stress.
    """
    return re.search(r'\d$', arpabet) != None


def stress(arpabet: str, stress: int):
    """Return arpabet with stress appended to the end if the given arpabet is a vowel.

    If the arpabet has stress added, return the arpabet as it is.
    If the arpabet is not a vowel, return the arpabet as it is.

    Arguments:
        arpabet {str} -- The given arpabet to add stress to.
        stress {int} -- The stress to be added (range from 0 - 2 inclusive)

    Returns:
        str -- The arpabet with stress appended to the end if the given arpabet is a vowel.
    """
    if not has_stress(arpabet) and arpabet in VOWELS:
        return arpabet.strip() + str(stress)
    return arpabet


def destress(arpabet: str):
    """Return arpabet with stress removed from the given arpabet.

    Arguments:
        arpabet {str} -- The given arpabet to have stress removed.

    Returns:
        [type] -- The arpabet with stress removed from the given arpabet.
    """
    return re.sub(r'\d$', '', arpabet.strip())
