# Minpair

Generate minimal pairs (and minimal sets).

> In phonology, minimal pairs are pairs of words or phrases in a particular language, spoken or signed, that differ in only one phonological element
>
> -- <cite>https://en.wikipedia.org/wiki/Minimal_pair</cite>

```
>>> import minpair
>>> minpair.vowel_minpair(['AE', 'EH'])
[{'AE': 'al', 'EH': 'l'}, {'AE': 'axe', 'EH': 'x'}, {'AE': 'bad', 'EH': 'bed'}, {'AE': 'bag', 'EH': 'beg'}]
```
