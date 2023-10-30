#!/usr/bin/env python
# coding: utf-8

# In[11]:


# R$60 por dia
# R$0.15 por Km rodado

dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos Km foram rodados? "))
pago = (dias * 60) + (km * 0.15)


print(f"\nO carro foi alugado por {dias} dias e rodou {km}km !")
print(f"O preço total a pagar é: R${pago:.2f} !!!")

