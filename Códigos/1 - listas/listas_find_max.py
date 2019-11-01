# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:37:01 2019

@author: Gustavo

problema: achar o maximo valor de uma lista
"""

lista = [3, 7, 8, 11, -2]

max_num = lista[0]

i = 0

while i < len(lista):
    if lista[i] > max_num:
        max_num = lista[i]
    i = i + 1
    
print("o maior elemento é ", max_num)