#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = str(input('Digite seu nome completo: ')).strip()


print(f'\nSeu nome tem Silva: {"SILVA" in nome.upper()}')

