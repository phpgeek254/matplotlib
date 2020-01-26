#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:22:00 2020

@author: maundaalex

use this plot to show correlations between two or more entities.

"""

import matplotlib.pyplot as plt
import random


test_scores = random.sample(range(10, 100), 40)
time_spent  = random.sample(range(10, 50), 40)

plt.scatter(time_spent, test_scores)
plt.xlabel("time spent on the test score")
plt.ylabel("Score on the test")

plt.show() 

# Plotting multiple groups of data.
x = [x for x in range(0, 5)]

y1 = random.sample(range(10, 20), 5)
y2 = random.sample(range(1, 10), 5)

plt.scatter(x, y1, marker="*", color="r")
plt.scatter(x, y2, marker="o", color="g")

plt.show()