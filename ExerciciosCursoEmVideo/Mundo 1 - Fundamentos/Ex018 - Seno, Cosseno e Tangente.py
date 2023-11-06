#!/usr/bin/env python
# coding: utf-8

# In[11]:


import math


angulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print(f'\nO SENO de {angulo}° é: {seno:.2f}!')

cosseno = math.cos(math.radians(angulo))
print(f'\nO COSSENO de {angulo}° é: {cosseno:.2f}!')

tangente = math.tan(math.radians(angulo))
print(f'\nA TANGENTE de {angulo}° é: {tangente:.2f}!')

