#!/usr/bin/env python
# Solution to Project Euler problem 26 - Reciprocal cycles
import numpy as np


if __name__ == '__main__':
    d = np.arange(1, 1000, 2)      # build array of all numbers up to N
    d = d[d % 5 != 0]              # remove multiples of 2 and 5 to simplify algorithm later
    k = np.ones(len(d))            # vector to track digits in period

    r = 10 % d
    while any(r != 0):             # loop until all elements are 0
        c = (r != 1) & (r != 0)    # mask to exclude complete elements in array
        r = (r * (10 * c)) % d     # remainder * 10 % divisor
        k += 1 * c                 # increment any included elements

    print(d[np.argmax(k)])         # get the divisor with the longest period
