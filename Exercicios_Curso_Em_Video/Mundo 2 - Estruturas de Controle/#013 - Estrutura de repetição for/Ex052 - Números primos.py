#!/usr/bin/env python
# coding: utf-8

# In[13]:


'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''


num = int(input('Digite um número inteiro: '))
tot = 0


for valor in range(1, num+1):
    if num % valor == 0:
        print("\033[33m", end='')
        tot += 1
    else:
        print("\033[31m", end='')
    print(f'{valor}', end=' ')
        
print('\n\033[mO número {} é divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

