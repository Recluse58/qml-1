#!/usr/bin/env python
from __future__ import division

from qform import qform

import sympy
from sympy import Rational as R


posarg = [0, R(1, 4), R(1, 3), R(1, 2), R(3, 4), 1, 2, 3]

def unique(items):
    return sorted(set(items))

def test_sqrt():
    for arg in unique(posarg + [8, 9]):
        output(qform(arg))


def tests():
    test_sqrt()


if __name__ == "__main__":
    def output(s):
        print s
    tests()
