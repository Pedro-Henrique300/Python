#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
    No final, mostre os 10 primeiros termos dessa progressão.'''


termo = int(input('Informe o 1º termo: '))
razão = int(input('Infome o razão: '))
décimo = termo + (10 - 1) * razão


for num in range(termo, décimo + razão, razão):
    print(num, end=' ➟ ')
    
print('Acabou')

