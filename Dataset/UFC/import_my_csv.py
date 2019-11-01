# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:32:26 2019

@author: Gustavo
"""

import csv
with open('preprocessed_data.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)
print(len(your_list))