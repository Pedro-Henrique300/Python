#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Para cada 2m² será usado 1L de tinta.

lar = float(input("Informe a largura da parede: "))
alt = float(input("Informe a altura da parede: "))
area = lar * alt
tinta = area / 2


print(f"\nSua parede tem a dimenção de {lar} X {alt} e possue uma área de {area}m²")
print(f"\nCom uma área de {area}m² você precisará de {tinta}L de tinta!!")

