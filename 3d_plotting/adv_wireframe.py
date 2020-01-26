#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:06:41 2020

@author: maundaalex
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np



fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()

ax1.plot_wireframe(x, y, z)

dx, dy, dz = np.ones(10), np.ones(10), x

ax1.bar3d(x, y, z, dx, dy, dz)

plt.show()