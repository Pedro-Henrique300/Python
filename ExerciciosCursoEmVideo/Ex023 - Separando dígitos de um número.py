#!/usr/bin/env python
# coding: utf-8

# In[16]:


num = int(input('Digite um número entre 1 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'\nUnidade: {u}.\nDezena: {d}.\nCentena: {c}.\nMilhar: {m}.')

