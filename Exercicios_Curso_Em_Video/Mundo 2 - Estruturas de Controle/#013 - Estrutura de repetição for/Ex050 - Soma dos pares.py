#!/usr/bin/env python
# coding: utf-8

# In[23]:


'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
    Se o valor digitado for ímpar, desconsidere-o.'''


valor = 0
soma = 0

for num in range(1, 7):
    
    valor = int(input('Digite um valor: '))
    
    if valor % 2 == 0:
        soma += valor
        
print(f'\nA soma dos números pares é: {soma}')

