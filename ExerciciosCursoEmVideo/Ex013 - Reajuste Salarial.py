#!/usr/bin/env python
# coding: utf-8

# In[8]:


salario = float(input('Qual o salário do Funcionário? R$'))
salario_aumento = salario + (salario * 15 / 100)


print(f'\nO Funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario_aumento}!')

