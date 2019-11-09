# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:09:56 2019

@author: Gustavo
"""

arq = open("teste.txt", encoding='utf-8') # encoding serve para pegar acentuação
print(arq.read(5))
print()
print(arq.readline())
print(arq.read())
