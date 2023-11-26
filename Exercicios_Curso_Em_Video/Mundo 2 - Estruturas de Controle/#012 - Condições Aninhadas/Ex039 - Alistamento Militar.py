#!/usr/bin/env python
# coding: utf-8

# In[18]:


''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
    se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''



from datetime import date


sexo = str(input('Informe seu sexo: ')).strip().upper()

if sexo == 'MASCULINO':

    nasc = int(input('Informe seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc


    print(f'Quem nasceu em {nasc} tem {idade} ano(s) em {ano_atual}.')


    if idade < 18:
        saldo = 18 - idade 
        print(f'Você ainda vai se alistar! Faltam {saldo} ano(s).')
        ano = ano_atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade == 18:
        print('Está na hora de se alistar!')
    else:
        saldo = idade - 18
        print(f'Já passou da idade de se alistar! Deveria ter se alistado há {saldo} ano(s).')
        ano = ano_atual - saldo
        print(f'Seu alistamento foi em {ano}')

else:
    print('\nVocê não precisa se alistar obrigatoriamente!')

