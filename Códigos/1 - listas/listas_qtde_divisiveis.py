# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:12:26 2019

@author: Gustavo

Problema: Escreva um código capaz de achar quantos números são divisíveis por 5 e por 7 (ao mesmo tempo), entre 1500 e 2700.

"""

n = 0 # qtde de numeros divisiveis por 5 e por 7
numeros = []

i = 1500 # valor inicial que vai ser alterado ao longo das iterações

while i <= 2700:
    
    if i%5 == 0 and i%7 == 0:
        n = n+1
        numeros.append(i)
    
    i = i + 1

print(n)
print(numeros)