#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 01:18:12 2020

@author: maundaalex

Use numpy to load the values instead  of doing a for loop. 
Its much easier
"""

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data.csv', delimiter=',', unpack=True);

print(x, y)
plt.plot(x, y, label="Loaded csvfile")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Values from a csv file")
plt.legend()
plt.show()
        

