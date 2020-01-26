#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:34:32 2020

@author: maundaalex

Show how data stacks up. A way to visualize parts of a whole
"""


import matplotlib.pyplot as plt
import random

year = [x for x in range(1, 11)]

print(year)

taxes =  random.sample(range(10, 30), 10)
overhead = random.sample(range(10, 40), 10)
entertainment = random.sample(range(10, 30), 10)

# Hack for creating legends
plt.plot([], [], color="r", label="Taxes")
plt.plot([], [], color="b", label="overhead")
plt.plot([], [], color="g", label="Entertainment")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Cost in thousands")
plt.title("Company Expences")

plt.stackplot(year, taxes, overhead, entertainment)


