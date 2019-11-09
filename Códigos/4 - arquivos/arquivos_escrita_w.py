# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:27:32 2019

@author: Gustavo
"""

arq = open("criando_arquivo.txt", "w")
arq.write("Sobreescrevendo o arquivo :)")
arq.close()

#open and read the file after the appending:
arq = open("criando_arquivo.txt", "r")
print(arq.read()) # perceba que abrir no modo "w" me faz perder todo o contéudo prévio