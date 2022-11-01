#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

# set height of bar
IT = [3448.0, 3463.3, 3524.3, 3567.6,3711.2,3663.8]
ECE = [-560.2,-669.1,-722.4,-931.7,-1047.0,-3146.9]

# Set position of bar on X axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# Make the plot
plt.bar(br1, IT, color ='b', width = barWidth,
		edgecolor ='grey', label ='Fed Govt Current Receipts')
plt.bar(br2, ECE, color ='r', width = barWidth,
		edgecolor ='grey', label ='Net Federal Govt Savings')


# Adding Xticks
plt.ylabel('Dollars in Billions', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],
		['2015', '2016', '2017', '2018', '2019','2020'])
plt.title('US Govt Receipts & Net Savings')

plt.legend()
plt.show()
