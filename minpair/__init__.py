from .generator import Generator


def generator(**args):
    return Generator(**args)


def vowel_minpair(vowels: list, pos: list = []):
    return generator().vowel_minpair(vowels, pos)


__all__ = ['__version__']
try:
    from ._version import version as __version__
except ImportError:
    # broken installation, we don't even try
    # unknown only works because we do poor mans version compare
    __version__ = 'unknown'
