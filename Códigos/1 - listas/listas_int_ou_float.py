# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:02:52 2019

@author: Gustavo
"""

n_usuario = input("Insira o numero desejado: ")

i = 0

print("o tamanho da minha string é = ", len(n_usuario))

while i < len(n_usuario):
    if n_usuario[i] == '.':
        print("É float!")
        n_usuario = float(n_usuario)
        break
    i = i + 1
    
print(n_usuario)