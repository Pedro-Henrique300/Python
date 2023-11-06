#!/usr/bin/env python
# coding: utf-8

# In[35]:


seg1 = float(input('Informe o 1º segmento: '))
seg2 = float(input('Informe o 2º segmento: '))
seg3 = float(input('Informe o 3º segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('\nOs segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('\nOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')

