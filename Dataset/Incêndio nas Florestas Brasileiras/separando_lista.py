# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:40:29 2019

@author: Gustavo
"""

lista = [['meu teste, 12'],['meu teste, 11'],['meu teste, 14']]

nova_lista = []
for item in lista:
    for subitem in item:
        #print(subitem)
        nova_lista.append([x.strip() for x in subitem.split(',')])
        
print(nova_lista[0][0].replace(".",""))