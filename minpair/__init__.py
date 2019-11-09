from minpair.generator import Generator


def generator(**args):
    return Generator(**args)


def vowel_minpair(vowels: list):
    return generator().vowel_minpair(vowels)


__all__ = ['__version__']
try:
    from minpair._version import version as __version__
except ImportError:
    # broken installation, we don't even try
    # unknown only works because we do poor mans version compare
    __version__ = 'unknown'
