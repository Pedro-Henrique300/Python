#!/usr/bin/env python
# coding: utf-8

# In[10]:


''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))


if num1 < num2:
    print('\nO SEGUNDO número é maior!')
elif num1 > num2:
    print('\n O PRIMEIRO número é maior!')
else:
    print('\nOs números são IGUAIS!')

