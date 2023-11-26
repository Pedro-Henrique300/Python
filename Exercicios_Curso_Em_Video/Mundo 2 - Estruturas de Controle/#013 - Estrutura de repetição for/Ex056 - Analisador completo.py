#!/usr/bin/env python
# coding: utf-8

# In[48]:


'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
    a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''


media = 0
media_idade = 0
mais_velho = 0
mulher_menor = 0
nome_velho = ''

for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    print('\n')
    
    media += idade
    
    if sexo == 'M':
        if idade > mais_velho:
            mais_velho = idade
            nome_velho = nome
    elif sexo == 'F' and idade < 20:
        mulher_menor += 1

media_idade = media / 4

print(f'\nA idade média desse grupo é de: {media_idade:.1f} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}.')
print(f'No grupo há {mulher_menor} mulher(es) menor(es) de 20 anos.')

