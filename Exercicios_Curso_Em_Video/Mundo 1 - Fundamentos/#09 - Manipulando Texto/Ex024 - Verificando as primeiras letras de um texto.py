#!/usr/bin/env python
# coding: utf-8

# In[28]:


'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input('Digite a cidade que você nasceu: ')).strip()
partes = cidade.upper().split()

'SANTO' in partes[0]

