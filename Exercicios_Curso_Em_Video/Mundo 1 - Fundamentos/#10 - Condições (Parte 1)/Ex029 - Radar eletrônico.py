#!/usr/bin/env python
# coding: utf-8

# In[32]:


velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade >80:
    print('MULTADO!!! Você exedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'E terá que pagar uma multa de R${multa:.2f}!')
    
print('\nDirija com cuidado!!! Tenha um bom dia!')

