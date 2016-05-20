import random, string
from collections import defaultdict, Counter

def word_counts(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary whose keys are all the words in the file (broken by
    whitespace). The value for each word is a dictionary containing each word
    that can follow the key and a count for the number of times it follows it.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Example:
    >>> #example.txt is a file containing: "The cat chased the dog"
    >>> with open('example.txt') as f:
    ...     word_counts(f)
    {'the': {'dog': 1, 'cat': 1}, 'chased': {'the': 1}, 'cat': {'chased': 1}}
    '''
    dictionary = defaultdict(Counter)
    words = list(map(lambda word: word.lower().strip(string.punctuation), f.read().split()))
    length = len(words)
    for i, word in enumerate(words):
        if i + 1 < length:
            post = words[i+1]
            dictionary[word][post] += 1
    return dictionary


def associated_words(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of two consecutive words in
    the file and the value for each key is a list of words that were found
    directly following the key.

    Words should be included in the list the number of times they appear.

    Example:
    >>> with open('alice.txt') as f:
    ...     d = associated_words(f)
    >>> d[('among', 'the')]
    ['people', 'party.', 'trees,', 'distant', 'leaves,', 'trees', 'branches,', 'bright']
    '''
    dictionary = defaultdict(set)
    words = list(map(lambda word: word.lower().strip(string.punctuation), f.read().split()))
    length = len(words)
    for i, w1 in enumerate(words):
        if i + 2 < length:
            w2 = words[i+1]
            w3 = words[i+2]
            dictionary[(w1, w2)].add(w3)
    return dictionary


if __name__ == '__main__':
    f = open('alice.txt')
    word_counts(f)
    associated_words(f)
