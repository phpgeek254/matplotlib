#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:50:27 2020

@author: maundaalex
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 3, 4, 5, 3, 8, 2, 2, 2]
z = [4, 4, 3, 5, 6, 6, 3 ,6, 7 ,1]

ax1.plot_wireframe(x, y, z)

#set the axis 
ax1.set_xlabel("x Axis")
ax1.set_ylabel("y Axis")
ax1.set_zlabel("z Axis")

plt.show()
