import markovify
import nltk
import re


class RangeDict(dict):
    """
    Enables a dictionary whose keys are ranges.

    Overrides `__getitem__` to handle keys that are ranges.
    """

    def __getitem__(self, item):
        if type(item) != range:
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)


class POSifiedText(markovify.Text):
    """
    A markovify.Text model that obeys sentence structure better than the naive model.

    Uses NLTK's part-of-speech tagger (nltk.pos_tag), which is VERY slow but seems to do a better
    job of parsing my text corpora than spaCy, which would be faster.
    """

    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = ["::".join(tag) for tag in nltk.pos_tag(words)]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
