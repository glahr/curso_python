# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:32:26 2019

@author: Gustavo
"""

import csv

with open('amazon.csv', 'r') as f:
    reader = csv.reader(f)
    minha_lista = list(reader)

print(len(minha_lista))

i = 1
while i < len(minha_lista):
    minha_lista[i][3] = float(minha_lista[i][3])
    i = i + 1

print(minha_lista)