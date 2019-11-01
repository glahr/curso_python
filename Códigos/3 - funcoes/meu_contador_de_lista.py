# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:04:59 2019

@author: Gustavo
"""

def meu_len(lista):
    i = 0
    try:
        while True:
            lista[i]
            i = i + 1
    except:
        return i

lista = [1, 2, 3, 4, 10, 11, 12]

n = meu_len(lista)
print(n)