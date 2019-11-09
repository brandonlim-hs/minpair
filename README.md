# Minpair

Generate minimal pairs (and minimal sets) for US English words.

> In phonology, minimal pairs are pairs of words or phrases in a particular language, spoken or signed, that differ in only one phonological element
>
> -- <cite>https://en.wikipedia.org/wiki/Minimal_pair</cite>

```python
>>> import minpair
>>> minpair.vowel_minpair(['AE', 'EH'])[:4]
[{'AE': 'al', 'EH': 'l'}, {'AE': 'axe', 'EH': 'x'}, {'AE': 'bad', 'EH': 'bed'}, {'AE': 'bag', 'EH': 'beg'}]
```

# Installation

```
pip install -U minpair
```

```python
>>> import minpair
```

# Usage

## Vowel minimal pairs

Words that differ in only one vowel phonological element. For example: b**a**d, b**e**d

```python
>>> minpair.vowel_minpair(['AE', 'EH'])[:4]
[{'AE': 'al', 'EH': 'l'}, {'AE': 'axe', 'EH': 'x'}, {'AE': 'bad', 'EH': 'bed'}, {'AE': 'bag', 'EH': 'beg'}]
```

# Config

## Corpus data

This package depends on a few NLTK's corpora, namely: _brown_, _cmudict_, _universal_tagset_, and _words_ corpus.
By default, this package will download these corpora into [NLTK data directory](https://www.nltk.org/data.html#command-line-installation) if not available.

To disable the auto download of corpus data:

```python
>>> minpair.generator(download_corpus=False).vowel_minpair(['AE', 'EH'])[:4]
[{'AE': 'al', 'EH': 'l'}, {'AE': 'axe', 'EH': 'x'}, {'AE': 'bad', 'EH': 'bed'}, {'AE': 'bag', 'EH': 'beg'}]
```

## POS

This package depends on part-of-speech tagger to filter words from meaningful lexical categories.
List of possible POS tags are found [here](https://universaldependencies.org/u/pos/).
By default, this package will only return words that are tagged as 'ADJ', 'NOUN' or 'VERB'.

To use different POS tags:

```python
>>> minpair.generator(pos=['VERB']).vowel_minpair(['AE', 'EH'])[:4]
[{'AE': 'bag', 'EH': 'beg'}, {'AE': 'bat', 'EH': 'bet'}, {'AE': 'blast', 'EH': 'blest'}, {'AE': 'kept', 'EH': 'kept'}]
```

Alternatively, using method chaining:

```python
>>> minpair.generator().pos(['VERB']).vowel_minpair(['AE', 'EH'])[:4]
[{'AE': 'bag', 'EH': 'beg'}, {'AE': 'bat', 'EH': 'bet'}, {'AE': 'blast', 'EH': 'blest'}, {'AE': 'kept', 'EH': 'kept'}]
```
