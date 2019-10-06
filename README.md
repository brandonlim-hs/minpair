# Minpair

Generate minimal pairs (and minimal sets) for US English words.

> In phonology, minimal pairs are pairs of words or phrases in a particular language, spoken or signed, that differ in only one phonological element
>
> -- <cite>https://en.wikipedia.org/wiki/Minimal_pair</cite>

```
>>> import minpair
>>> minpair.vowel_minpair(['AE', 'EH'])[:4]
[{'AE': 'al', 'EH': 'l'}, {'AE': 'axe', 'EH': 'x'}, {'AE': 'bad', 'EH': 'bed'}, {'AE': 'bag', 'EH': 'beg'}]
```

# Installation

```
pip install minpair
```

# Dependencies

## NLTK

This package depends on a few NLTK's corpora, namely: _brown_, _cmudict_, _universal_tagset_, and _words_ corpus.
This package will download these corpora into [NLTK data directory](https://www.nltk.org/data.html#command-line-installation) if not available.
