# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:53:52 2019

@author: Gustavo
"""

print("Olá! Vamos criar uma lista juntos.\n Quando vc quiser parar, digite \"chega\".")

lista = []

n = input("Insira um elemento na lista: ")

while n != 'chega':
    lista.append(int(n))
    n = input("Insira outro elemento na lista: ")

print(lista)