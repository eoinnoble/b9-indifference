import re
from collections.abc import MutableMapping
from typing import Dict, List

import markovify
import nltk


class RangeDict(MutableMapping):
    """Enables a dictionary whose keys are ranges."""

    def __init__(self, iterable: Dict):
        if not isinstance(iterable, dict):
            raise TypeError("You must pass a dictionary to RangeDict")

        self.store = dict()

        for (k, v) in iterable.items():
            if not isinstance(k, range):
                raise TypeError("Your dictionary keys must be ranges")

            direction = {num: v for num in k}
            self.store.update(direction)

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)


class POSifiedText(markovify.Text):
    """
    A markovify.Text model that obeys sentence structure better than the naive model.

    Uses NLTK's part-of-speech tagger (nltk.pos_tag), which is VERY slow but seems to do a better
    job of parsing my text corpora than spaCy, which would be faster.
    """

    def word_split(self, sentence: str) -> List:
        words = re.split(self.word_split_pattern, sentence)
        words = ["::".join(tag) for tag in nltk.pos_tag(words)]
        return words

    def word_join(self, words: List) -> str:
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
