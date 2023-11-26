#!/usr/bin/env python
# coding: utf-8

# In[26]:


'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
    Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, 
    ANOTARAM A DATA DA MARATONA.'''


frase = str(input('Digite uma frase: ')).strip().upper()
partes = frase.split()
junta = ''.join(partes)
inverso = ''

for letra in range(len(junta)-1, -1, -1):
    inverso += junta[letra]

print(f'\nO inverso de {junta} é {inverso}')
    
if inverso == junta:
    print('\nTemos um palíndromo!')
else:
    print('\nA frase digitada não é um palíndromo!')

