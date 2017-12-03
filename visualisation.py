#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 3ngthrust
"""

import matplotlib.pyplot as plt

x = list(range(1995,2018,1))
songa_values = [5470, 1546, 9318, 10523, 14666, 16185, 2401, 5657, 4702, 5416, 10600, 6919, 9637, 11307, 11765, 18171, 20229, 17606, 13071, 20805, 26996, 19403, 5269]

fig = plt.figure(1)
plt.plot(x, songa_values, marker='o', label="Max Martin") 

plt.title('Chart Success of Max Martin')
plt.xlabel('Year')
plt.ylabel('Chart Success (Accumulated Song Values)')
#plt.legend(loc='upper left')

fig.savefig('Max_Martin_Chart_Success.png', dpi = 300)

plt.show()
