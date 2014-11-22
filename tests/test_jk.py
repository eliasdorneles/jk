#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jk
----------------------------------

Tests for `jk` module.
"""

import unittest

import jk


def simple_gen():
    return (x for x in range(5))


class TestJk(unittest.TestCase):

    def test_each_cons_work_with_generators(self):
        self.assertEquals([(0, 1), (1, 2), (2, 3), (3, 4)],
                          list(jk.each_cons(simple_gen(), 2)))

    def test_each_cons_yelds_nothing_when_iterable_ends_earlier(self):
        self.assertEquals([], list(jk.each_cons(range(4), 5)))

    def test_first_from_any_iterable(self):
        self.assertEquals('first', jk.first(['first', 'second']))
        self.assertEquals(1, jk.first(range(1, 5)))
        self.assertEquals(0, jk.first(simple_gen()))
        self.assertEquals('default', jk.first([], 'default'))

    def test_second_from_any_iterable(self):
        self.assertEquals('second', jk.second(['first', 'second']))
        self.assertEquals(2, jk.second(range(1, 5)))
        self.assertEquals(1, jk.second(simple_gen()))
        self.assertEquals('default', jk.second([], 'default'))

    def test_slice_before_simple(self):
        # setup:
        numbers = (x for x in [2, 3, 111, 4, 5, 6, 7, 111])

        # when:
        result = jk.slice_before(lambda x: x == 111, numbers)

        # then:
        self.assertEquals(
            [(2, 3), (111, 4, 5, 6, 7), (111,)],
            list(result)
        )

    def test_slice_before_when_first_element_matches(self):
        # setup:
        numbers = [111, 2, 3, 111, 4, 5, 6, 7, 111]

        # when:
        result = jk.slice_before(lambda x: x == 111, numbers)

        # then:
        self.assertEquals(
            [(111, 2, 3), (111, 4, 5, 6, 7), (111,)],
            list(result)
        )

    def test_slice_after_simple(self):
        # setup:
        numbers = (x for x in [111, 2, 3, 111, 4, 5, 6, 7, 111])

        # when:
        result = jk.slice_after(lambda x: x == 111, numbers)

        # then:
        self.assertEquals(
            [(111,), (2, 3, 111), (4, 5, 6, 7, 111)],
            list(result)
        )


if __name__ == '__main__':
    unittest.main()
