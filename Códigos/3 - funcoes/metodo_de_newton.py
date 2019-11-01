# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:57:23 2019

@author: Gustavo
"""

def funcao(x):
    y = 3*x**7 + 1.5*x**3 + 4*x + 1
    #raiz é -0.24448
    return y

def derivada(x):
    der = 21*x**6 + 4.5*x**2 + 4
    return der

x = 0
x_ant = x
erro = 10
y_desejado = 0

while erro > 0.001:
    x = x_ant - funcao(x)/derivada(x)
    erro = abs(y_desejado - funcao(x))
    print(x)
    x_ant = x