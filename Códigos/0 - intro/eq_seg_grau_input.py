# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:30:03 2019

@author: Gustavo
"""

a = float(input("insira o valor de a = "))
b = float(input("insira o valor de b = "))
c = float(input("insira o valor de c = "))
delta = b**2 - 4*a*c
x1 = (-b+delta**0.5)/(2*a)
x2 = (-b-delta**0.5)/(2*a)
print("as raizes sao:")
print("x1 = ", x1)
print("x2 = ", x2)