#!/usr/bin/env python
# coding: utf-8

# In[7]:


preco = float(input('Qual é o preço do produto? '))
preco_desconto = preco - (preco * 5 / 100)


print(f'\nO produto que custava R${preco} com 5% de desconto passa a custar R${preco_desconto} !') 

