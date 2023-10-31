#!/usr/bin/env python
# coding: utf-8

# In[18]:


C = float(input('Informe o valor a ser investido: R$ '))
I = float(input('Informe a taxa de CDI atualmente ( sem % por favor ): '))


t = 100 + I
t /= 100


for mes in range(1, 13):
    C *= t
    print('______________________________________')
    print(f'| No {mes}º mês você estará com R${C:.2f}! |')
    print('--------------------------------------')

