#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 01:27:27 2020R

@author: maundaalex
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#import matplotlib.ticker as mticker
#from mpl_finance import candlestick_ohlc
import numpy as np
from matplotlib import style

style.use('seaborn-poster')

#show all styles
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

#candlestick_ohlc
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

x=0
y= len(date)
new_list= []

while x < y:
    line = date[x], closep[x], highp[x], lowp[x], openp[x], adjclose[x], volume[x]
    new_list.append(line)
    x+=1
    
#candlestick_ohlc(ax1, new_list)
#plt.show()


ax1.axhline(20, color='g')
ax1.axhline(10, color='r')
plt.plot_date(date, closep, "-")

#using a fill
plt.fill_between(date, closep, 20,  where=(closep>20), facecolor="g", alpha=.5)
plt.fill_between(date, closep, 10,  where=(closep<10), facecolor="r", alpha=.5)

#Adjusted the spaces.
plt.subplots_adjust(
        left=.09, 
        bottom=.16, 
        right=.94, 
        top=.95, 
        wspace=.2, 
        hspace=.5
                    )

for l in ax1.xaxis.get_ticklabels():
    l.set_rotation(45)

ax1.grid(True, color='g')
plt.show()
