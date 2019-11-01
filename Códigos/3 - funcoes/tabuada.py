# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:36:22 2019

@author: Gustavo
"""

def tabuada(x):
    tab = []
    for i in range(1,11):
        tab.append(i*x)
    return tab
#     return [i*x for i in range(1,11)]

numero = 7
print(tabuada(numero))