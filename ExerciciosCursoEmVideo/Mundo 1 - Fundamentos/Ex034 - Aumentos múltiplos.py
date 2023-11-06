#!/usr/bin/env python
# coding: utf-8

# In[32]:


'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
                 Para salários superiores a R$1250,00, calcule um aumento de 10%. 
                    Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Informe o salário do(a) funcionário(a): '))

if salario > 1250.00:
    print(f'\nO salário recebeu um aumento de {salario + (salario * 10 / 100):.2f}')
else:
    print(f'\nO salário recebeu um aumento de {salario + (salario * 15 / 100):.2f}')

