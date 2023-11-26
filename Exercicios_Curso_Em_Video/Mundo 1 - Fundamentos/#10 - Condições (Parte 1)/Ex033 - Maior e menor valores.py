#!/usr/bin/env python
# coding: utf-8

# In[29]:


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
    
print(f'\nO maior valor é {maior}.')

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
    
print(f'O menor valor é {menor}. ')

