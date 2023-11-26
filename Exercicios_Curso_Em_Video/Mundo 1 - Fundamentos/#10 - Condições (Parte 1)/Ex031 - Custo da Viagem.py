#!/usr/bin/env python
# coding: utf-8

# In[13]:


'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
        cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('Qual é a distancia da sua viagem? '))
print(f'\nVocê está prestes a começar uma viagem de {distancia}Km')

if distancia <= 200:
    print(f'O preço da sua passagem será de R${distancia * 0.50:.2f}!')
else:
    print(f'O preço da sua passagem será de R${distancia * 0.45:.2f}!')

