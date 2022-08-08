#!/usr/bin/env python
# Solution to Project Euler problem 44 - Pentagon numbers
import numpy as np


N = 3000
if __name__ == '__main__':
    pn = np.arange(1, N + 1)                                    # build array of all numbers 1..N
    pn = pn * (3 * pn - 1) / 2                                  # compute pentagon numbers for 1..N

    c = np.take(np.meshgrid(pn, pn), np.tril_indices(N, -1))    # get all combinations of size 2

    s = np.sum(c, axis=0)                                       # compute all sums of numbers
    d = c[0, :] - c[1, :]                                       # compute all differences of numbers
    i = np.intersect1d(np.where(np.in1d(s, pn))[0],             # get all sums and differences that are pentagonal
                       np.where(np.in1d(d, pn))[0])             # intersect sum and difference indices
    print(min(d[i]))                                            # print the minimum difference value


