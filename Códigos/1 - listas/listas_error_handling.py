# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:12:47 2019

@author: Gustavo
"""

n_usuario = input("Insira o numero desejado: ")

try:
    n_usuario = int(n_usuario)
    
except:
    try:
        n_usuario = float(n_usuario)
    except:
        print("É pra ser um numero!")
        
print("meu numero é: ", n_usuario)
print(type(n_usuario))