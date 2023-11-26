#!/usr/bin/env python
# coding: utf-8

# In[40]:


''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
    calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
    de acordo com a tabela abaixo:
    
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''



peso = float(input('Informe seu peso(Kg): '))
altura  = float(input('Informe sua altura(m): '))
IMC = peso / altura ** 2



print(f'''\nVocê possue um peso de {peso} Kg e uma altura de {altura:.2f} m
Seu IMC é: {IMC:.1f} 
STATUS: ''', end='')



if IMC < 18.5:
    print('Abaixo do Peso')
elif IMC <= 25:
    print('Peso Ideal')
elif IMC <= 30:
    print('Sobrepeso')
elif IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

