from nltk import download
from nltk.data import find


def require(corpora: list = []):
    """Download the required NLTK corpus if not found.

    Keyword Arguments:
        corpora {list} -- The identifier or name of NLTK corpus (default: {[]})
    """
    for corpus in corpora:
        try:
            find(corpus)
        except LookupError:
            download(corpus)
