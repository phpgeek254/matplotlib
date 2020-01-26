#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:57:08 2020

@author: maundaalex

Values are converted to percentages a a whole.
"""


import matplotlib.pyplot as plt

labels = 'Taxes', 'overhead', 'Entertainmant'

print(labels)

sizes = [25, 32, 12]

colors = ['c', 'm', 'b']

plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct="%1.1f%%",
        shadow=True, explode=(0.1, 0.1, 0.1))

plt.show()

