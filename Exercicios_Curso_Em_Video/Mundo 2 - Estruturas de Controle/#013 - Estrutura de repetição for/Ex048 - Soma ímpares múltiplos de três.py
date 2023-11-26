#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
    que se encontram no intervalo de 1 até 500'''


soma = 0
quant = 0

for mult in range(1, 501):
    if mult % 3 == 0 and mult % 2 == 1:
        soma += mult
        quant += 1
print(f'\nA soma de todos os {quant} valores múltiplos de 3 é: {soma}')

