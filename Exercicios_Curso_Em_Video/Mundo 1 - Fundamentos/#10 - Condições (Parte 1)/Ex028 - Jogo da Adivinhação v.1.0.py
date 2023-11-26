#!/usr/bin/env python
# coding: utf-8

# In[26]:


from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-'*15)
print('Eu irei pensar em um número inteiro de 0 a 5.')
print('E você terá que adivinhar...')
print('-=-'*15)

usuario = int(input('\nEm que número pensei? '))
print('\nPROCESSANDO...')
sleep(2)

if(usuario == computador):
    print('\nVocê acertou, PARABÉNS!!!')
else:
    print(f'\nVocê errou, eu pensei no número {computador} e não no {usuario}.')
    print('Tente novamente...')

