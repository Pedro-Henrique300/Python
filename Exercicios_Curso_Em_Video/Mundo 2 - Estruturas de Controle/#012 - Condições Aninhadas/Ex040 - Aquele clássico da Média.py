#!/usr/bin/env python
# coding: utf-8

# In[24]:


'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
   de acordo com a média atingida:
   
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''



nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2



print(f'''\nPrimeira nota: {nota_1}
Segunda nota: {nota_2}
Sua média foi de {media}
Situação: ''', end='')



if media < 5.0:
    print('REPROVADO!')
elif media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')

