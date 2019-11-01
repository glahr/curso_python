# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:22:20 2019

@author: Gustavo
"""

import random

def jogar_dado():
    print(random.randrange(1,7))

while True:
    input("Digite enter para jogar o dado.")
    jogar_dado()
    jogar_dado()