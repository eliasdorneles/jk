# -*- coding: utf-8 -*-

__author__ = 'Elias Dorneles'
__email__ = 'eliasdorneles@gmail.com'
__version__ = '0.1.0'


from itertools import islice, tee

try:
    from itertools import izip as zip
except ImportError:
    pass

try:
    string_type = basestring
except NameError:
    string_type = str

import re


def each_cons(sequence, size):
    """Iterates lazily through a sequence looking at a sliding window
    with given size, for each time.

    each_cons([1, 2, 3, 4], 2) --> [(0, 1), (1, 2), (2, 3), (3, 4)]
    """
    return zip(*(islice(it, start, None)
                 for start, it in enumerate(tee(sequence, size))))


def slice_before(predicate, iterable):
    """Returns groups of elements from iterable,
    slicing just before predicate(elem) is True
    """
    if isinstance(predicate, string_type):
        predicate = re.compile(predicate)

    if hasattr(predicate, 'match'):
        predicate = predicate.match

    record = []

    for i, item in enumerate(iterable):
        if i == 0:
            record = [item]
            continue

        if predicate(item):
            yield tuple(record)
            record = [item]
        else:
            record.append(item)

    if record:
        yield tuple(record)


def slice_after(predicate, iterable):
    """Returns groups of elements from iterable,
    slicing just after predicate(elem) is True
    """
    record = []
    for i, item in enumerate(iterable):
        record.append(item)

        if predicate(item):
            yield tuple(record)
            record = []

    if record:
        yield tuple(record)


def nth(iterable, n, default=None):
    """Returns the nth item or a default value

    Note that nth is an ordinal number, so this is not zero-indexed:
    use n=1 for first element, n=4 for fourth, and so on."""

    return next(islice(iterable, n - 1, None), default)


def first(iterable, default=None):
    "Returns the first item or a default value"
    return nth(iterable, 1, default)


def second(iterable, default=None):
    "Returns the second item or a default value"
    return nth(iterable, 2, default)

