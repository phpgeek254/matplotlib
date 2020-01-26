#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 01:27:27 2020R

@author: maundaalex
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import numpy as np
from matplotlib import style

style.use('seaborn-poster')

# show all styles
print(plt.style.available)


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)

    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)

    return bytes_converter


date, closep, highp, lowp, openp, adjclose, volume = np.loadtxt('data.csv', delimiter=',',
                                                                unpack=True,
                                                                converters={0: bytespdate2num('%Y-%m-%d')}
                                                                )

# candlestick_ohlc
fig = plt.figure()
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
plt.ylabel("Prices")
ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

x = 0
y = len(date)
new_list = []

while x < y:
    line = date[x], closep[x], highp[x], lowp[x], openp[x], adjclose[x], volume[x]
    new_list.append(line)
    x += 1

candlestick_ohlc(ax2, new_list)
ax1.grid(True, color='g')

ax1.plot()
ax3.plot()

# Change the oriantation of the x-axis annotations.
for l in ax1.xaxis.get_ticklabels():
    l.set_rotation(45)

# Add locators
ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))

# Add Formating
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

# Add annotation
ax2.annotate("oil spill",
             (date[-1], highp[-1]),
             xytext=(.8, .9),
             textcoords="axes fraction",
             arrowprops=dict(facecolor="r", color="g"))

# Add abox at the bottom of the chart

box_props = dict(boxstyle='round4, pad=3', fc="y", ec="k")

ax2.annotate(str(closep[-1]), date([-1], closep[-1]),
             xytext=(date[-1] + 8, closep[-1]), bbox=box_props)

# Adjusted the spaces.
plt.subplots_adjust(
    left=.09,
    bottom=.16,
    right=.94,
    top=.95,
    wspace=.2,
    hspace=.5
)

plt.show()
