# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:23:26 2019

@author: Gustavo
"""

lista = [10, 11, 12, 13]

i = 0

try:
    while i <= len(lista):
        print(lista[i])
        i = i+1
except IndexError:
    print("Meu amigo, a lista é menor do que isso!")
            