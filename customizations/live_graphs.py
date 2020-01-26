#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 04:30:50 2020

@author: maundaalex
"""

import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation


style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
def animate(i):
    data = open("example_data.csv", "r").read()
    data_list = data.split("\n")
    xs = [];
    ys = [];
    
    for line in data_list:
        if len(line) > 1:
            x, y = line.split(",")
            xs.append(x)
            ys.append(y)
            
            
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()