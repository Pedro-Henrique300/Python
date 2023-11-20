#!/usr/bin/env python
# coding: utf-8

# In[28]:


'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
  de acordo com a idade:
  
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''



from datetime import date



nasc = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc



print(f'\nO(A) atleta tem {idade} anos e vai participar da categoria: ', end='')



if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

