#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 04:59:31 2020

@author: maundaalex
"""

import matplotlib.pyplot as plt
from matplotlib import style   
import math

style.use("ggplot")

xs = [];
ys = [];

font = {
        "family" : "serif",
        "color" : "darkred",
        "size": 12
        }

for i in range(19):
    x = i
    y = math.sin(x)
    
    xs.append(x)
    ys.append(y)

plt.figure()
plt.subplot(812)    
plt.plot(xs, ys, "r--")
plt.show()