#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:46:20 2020

@author: maundaalex
"""

import matplotlib.pyplot as plt

# Pretty basic ggraph.
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5, 6]

x2 = [12, 20, 13, 14,15, 16]
y2 = [10, 2, 2, 7, 10, 0]

#Default.
#plt.plot(x, y, label ="Plots for y")
#plt.plot(x, y2, label="plots for y1")

# Bar
plt.bar(x, y, label ="Plots for y")
plt.bar(x2, y2, label="plots for y1")

# labels and title.
plt.xlabel("Plot Number")
plt.ylabel("Random Number")
plt.title("Smaple title for the lables")

#Legends.
plt.legend()

plt.show()
