# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:11:08 2019

@author: Gustavo
"""

import csv
import matplotlib.pyplot as plt

def abrir_csv():
    with open('amazon.csv', 'r') as f:
        reader = csv.reader(f)
        minha_lista = list(reader)
    return minha_lista

def separar_lista(lista):
    nova_lista = []
    for item in lista:
        for subitem in item:
            nova_lista.append([x.strip() for x in subitem.split(',')])
    return nova_lista

def limpar_lista(lista):
    i = 1
    while i < len(lista):
        lista[i][0] = int(lista[i][0])
        lista[i][1] = lista[i][1].replace("\"","")
        lista[i][2] = lista[i][2].replace("\"","")
        lista[i][3] = int(lista[i][3].replace(".",""))
        i = i + 1
    return lista


lista_incendios = abrir_csv()
lista_incendios = separar_lista(lista_incendios)
lista_incendios = limpar_lista(lista_incendios)

n_incendios_sp = []
n_incendios_mg = []
n_ano_sp = []
n_ano_mg = []
for ano, estado, mes, incendios, _ in lista_incendios:
    if estado == 'Sao Paulo' and mes == 'Setembro':
        n_incendios_sp.append(incendios)
        n_ano_sp.append(ano)
    if estado == 'Minas Gerais' and mes == 'Setembro':
        n_incendios_mg.append(incendios)
        n_ano_mg.append(ano)

plt.plot(n_ano_sp, n_incendios_sp,'g--')
plt.plot(n_ano_sp, n_incendios_sp,'yo')
plt.plot(n_ano_mg, n_incendios_mg,'r')
plt.show()