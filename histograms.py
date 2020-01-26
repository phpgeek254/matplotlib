#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:08:55 2020

@author: maundaalex
"""

import matplotlib.pyplot as plt
import random

test_scores =  random.sample(range(10, 100), 30)

x = [x for x in range(len(test_scores))]

#plt.bar(x, test_scores)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()


bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(test_scores, bins, histtype='bar', cumulative=True, rwidth=.8)
print(test_scores)