# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:24:13 2019

@author: Gustavo
"""

arq = open("teste_escrita.txt", "a") # lendo no modo de acrescentar

arq.write("\nMais uma linha para meu código!")
arq.close()

# agora vamos ler e ver o que aconteceu
arq = open("teste_escrita.txt", "r")
print(arq.read()) 
