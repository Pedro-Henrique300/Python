#!/usr/bin/env python
# coding: utf-8

# In[20]:


'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for'''


valor = int(input('Informe qual tabuda quer gerar: '))


for num in range(0, 11):
    print(f'{valor} X {num:2} = {valor * num}')

