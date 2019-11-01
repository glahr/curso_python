# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:15:54 2019

@author: Gustavo
"""

primos = []
for numero in range(2,1000):
    e_primo = True
    for primo in primos:
        if numero%primo == 0:
            e_primo = False
            break
    if e_primo == True:
        primos.append(numero)
    
primos.insert(0,1)
print(primos)