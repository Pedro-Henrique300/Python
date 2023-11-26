#!/usr/bin/env python
# coding: utf-8

# In[29]:


'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
   mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date 

maior_idade = 0
menor_idade = 0
ano_atual = date.today().year

for pessoa in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = ano_atual - nasc
    
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade +=1
        
print(f'\n{maior_idade} pessoa(s) são/é maior(es) de 18 anos!')
print(f'{menor_idade} pessoa(s) ainda são/é menor(es) de idade!')

