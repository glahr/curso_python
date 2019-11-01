# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:21:05 2019

@author: Gustavo
"""

try:
    while True:
        print("loop infinito!")
except (KeyboardInterrupt, IndexError):
    print("Operação abortada pelo usuario.")