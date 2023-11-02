#!/usr/bin/env python
# coding: utf-8

# In[12]:


nome = str(input('Digite seu nome completo: ')).strip()

print('\nAnalisando nome...\n')
print(f'Seu nome em maiúsculo fica assim: {nome.upper()}.')
print(f'Seu nome em minúsculo fica assim: {nome.lower()}.')
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
print(f'Seu primeiro nome é {nome.split()[0]} e ele possue {len(nome.split()[0])} letras!')

