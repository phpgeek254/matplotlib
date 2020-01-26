#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 01:05:20 2020

@author: maundaalex
"""
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data.csv', 'r') as csv_file:
    plots = csv.reader(csv_file, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot(x, y, label="Loaded csvfile")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Values from a csv file")
plt.legend()
plt.show()
        
