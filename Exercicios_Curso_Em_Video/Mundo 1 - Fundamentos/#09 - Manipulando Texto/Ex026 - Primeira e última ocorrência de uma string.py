#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
    em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip()


print(f'\nA letra "A" aparece {frase.upper().count("A")} vezes na sua frase.')
print(f'A primeira letra "A" apareceu na posição: {frase.upper().find("A")+1}')
print(f'A ultima letra "A" apareceu na posição: {frase.upper().rfind("A")+1}')

