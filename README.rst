===============================
JK python library
===============================

.. image:: https://badge.fury.io/py/jk.png
    :target: http://badge.fury.io/py/jk

.. image:: https://travis-ci.org/eliasdorneles/jk.png?branch=master
        :target: https://travis-ci.org/eliasdorneles/jk

.. image:: https://pypip.in/d/jk/badge.png
        :target: https://pypi.python.org/pypi/jk


Library containing useful functions for manipulating iterables.

Inspiration was drawn from Python itertools' recipes and Ruby's Enumerable API.

Works on Python 2.6+ and 3.x.

* Free software: BSD license
* Documentation: https://jk.readthedocs.org.

Features
--------

each_cons
:::::::::

* ``each_cons(sequence, size)``

Iterates lazily through a sequence, yielding a sliding window
with the given size for each iteration.

Examples:

Calculating quarterly sales report::

    >>> import jk
    >>> month_sales = [123.45, 54.3, 428.1, 144.2, 245.45, 197.3]
    >>> for a, b, c in jk.each_cons(month_sales, 3):
    ...     print '%0.2f' % ((a + b + c)/3)
    ...
    201.95
    208.87
    272.58
    195.65

Find duplicated lines in a file::

    >>> lines = """here is a simple
    ... file for us to test.
    ... this line repeats
    ... this line repeats
    ... -- this one does not
    ... this one repeats too
    ... this one repeats too
    ... okay, we're done here""".split('\n')
    >>>
    >>> for ln, (a, b) in enumerate(jk.each_cons(lines, 2), 1):
    ...     if a == b:
    ...         print (ln, a)
    ...
    (3, 'this line repeats')
    (6, 'this one repeats too')



slice_before and slice_after
::::::::::::::::::::::::::::

* ``slice_before(predicate, sequence)``
* ``slice_after(predicate, sequence)``

These functions are useful when you have a stream that has some sort of delimiter.
Handy for parsing log files, for example.

They iterate lazily through a sequence, yielding a tuple containing the elements
sliced just before (or after) the predicate evaluates to True.

The predicate argument can also be a string or a regular expression pattern
to be matched against the sequence elements.

Examples::

Grouping numbers until reaching zero::

    >>> numbers = [1, 2, 3, 0, 4, 5, 0, 6, 0, 7, 8]
    >>> print list(jk.slice_after(lambda x: x == 0, numbers))
    [(1, 2, 3, 0), (4, 5, 0), (6, 0), (7, 8)]

Reading entries of a fantasy multiline log file::

    >>> log_lines = """START: initiating...
    ... kernel found
    ... EVENT: started
    ... moving on
    ... EVENT: something happened
    ... EVENT: another thing happened""".split('\n')
    >>>
    >>> for entry in jk.slice_before('^(START|EVENT):', log_lines):
    ...     print entry
    ...
    ('START: initiating...', 'kernel found')
    ('EVENT: started', 'moving on')
    ('EVENT: something happened',)
    ('EVENT: another thing happened',)

first, second and nth
:::::::::::::::::::::

* ``first(sequence, default=None)``

Returns the first element of a sequence
(or a default value if the sequence is empty).

* ``second(sequence, default=None)``

Returns the second element of a sequence
(or a default value if not exists).

* ``nth(sequence, n, default=None)``

Returns the nth element of a sequence
(or a default value if not exists).

Note that the argument n is not a zero-based index: it is a ordinal number,
so n=1 means the first element, n=4 means the fourth and so on.

