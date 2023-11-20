#!/usr/bin/env python
# coding: utf-8

# In[4]:


''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100

print(f'\nPara pagar uma casa de {valor_casa:.2f} em {anos} anos', end='')
print(f' a prestação será de {prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

