#!/usr/bin/env python
# coding: utf-8

# In[5]:


''' Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
    indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep

print('Agora é contagem regressiva...')

for c in range(10, 0-1, -1):
    sleep(1)
    print(c)
    
print('Cabuuuum!')

