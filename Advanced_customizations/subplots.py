#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:28:01 2020

@author: maundaalex

Addition of multiple plot on one graph
"""


import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

#print put the plot types available
print("styles available:\n {}".format(plt.style.available))

fig = plt.figure()

def create_plots():
    xs = []
    ys = []
    
    for i in range(10):
        x = i
        y = random.randrange(8)
        
        xs.append(x)
        ys.append(y)
        
    return xs, ys
    
# create the first plot
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(325)
ax4 = fig.add_subplot(326)

x, y = create_plots()
ax1.plot(x, y)

x, y = create_plots()
ax2.plot(x, y)

x, y = create_plots()
ax3.plot(x, y)


x, y = create_plots()
ax4.plot(x, y)

plt.show()


