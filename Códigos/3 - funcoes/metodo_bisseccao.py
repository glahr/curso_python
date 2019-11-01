# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:36:40 2019

@author: Gustavo
"""
# este método só funciona se y(a) < 0 e y(b) > 0
def funcao(x):
    y = 3*x**7 + 1.5*x**3 + 4*x + 1
    return y

# iniciando as variaveis
a = -1
b = 1
y_desejado = 0
erro = 10
x_medio = (a+b)/2

# utilizando o método
while erro > 1e-10:
    print(x_medio)
    x_medio = (a+b)/2
    if funcao(x_medio) > 0:
        b = x_medio
    if funcao(x_medio) < 0:
        a = x_medio
    if funcao(x_medio) == 0:
        print("raiz exata")
        break
    erro = abs(y_desejado - funcao(x_medio))
    
print("a raiz é: ", x_medio)