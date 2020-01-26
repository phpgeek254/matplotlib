#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 01:27:27 2020

@author: maundaalex
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import yfinance as yf
import numpy as np

stock = yf.Ticker("tsla")

print(stock.info)
graph_data(stock)
