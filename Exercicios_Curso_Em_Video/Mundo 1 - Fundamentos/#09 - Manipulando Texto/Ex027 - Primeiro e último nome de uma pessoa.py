#!/usr/bin/env python
# coding: utf-8

# In[11]:


'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).strip()
partes = nome.split()

print('\nPrazer em te conhecer!!!')
print(f'Seu primeiro nome é: {partes[0]}.')
print(f'Seu último nome é: {partes[-1]}.')

