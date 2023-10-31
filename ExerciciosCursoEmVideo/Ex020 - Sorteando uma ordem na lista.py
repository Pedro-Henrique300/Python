#!/usr/bin/env python
# coding: utf-8

# In[19]:


from random import shuffle


aluno_1 = str(input('Informe o nome do(a) 1º aluno(a): '))
aluno_2 = str(input('Informe o nome do(a) 2º aluno(a): '))
aluno_3 = str(input('Informe o nome do(a) 3º aluno(a): '))
aluno_4 = str(input('Informe o nome do(a) 4º aluno(a): '))


lista = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista)


print('\nA ordem de apresentação será: ')
print(lista)

