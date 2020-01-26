#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:50:18 2020

@author: maundaalex
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np



fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 3, 4, 5, 3, 8, 2, 2, 2]
z = np.zeros(10)

dx, dy, dz = np.ones(10), np.ones(10), x

ax1.bar3d(x, y, z, dx, dy, dz)

plt.show()
