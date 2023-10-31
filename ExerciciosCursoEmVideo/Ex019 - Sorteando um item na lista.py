#!/usr/bin/env python
# coding: utf-8

# In[16]:


from random import choice

aluno_1 = input("Informe o nome do(a) 1º aluno(a): ")
aluno_2 = input("Informe o nome do(a) 2º aluno(a): ")
aluno_3 = input("Informe o nome do(a) 3º aluno(a): ")
aluno_4 = input("Informe o nome do(a) 4º aluno(a): ")
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista)

print(f'\nO aluno(a) escolhido(a) foi: {escolhido}')

