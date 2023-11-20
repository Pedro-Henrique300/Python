#!/usr/bin/env python
# coding: utf-8

# In[33]:


'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''



seg1 = float(input('Informe o 1º segmento: '))
seg2 = float(input('Informe o 2º segmento: '))
seg3 = float(input('Informe o 3º segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('\nOs segmentos acima PODEM FORMAR UM TRIÂNGULO!')
    print('Este triângulo é do tipo: ', end='')
    
    if seg1 == seg2 and seg2 == seg3 and seg3 == seg1:
        print('EQUILÁTERO')
    elif seg1 == seg2 != seg3 or seg2 == seg3 != seg1 or seg3 == seg1 != seg2:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('\nOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')

