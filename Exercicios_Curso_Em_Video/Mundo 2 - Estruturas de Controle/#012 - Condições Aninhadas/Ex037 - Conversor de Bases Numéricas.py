#!/usr/bin/env python
# coding: utf-8

# In[7]:


''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
                                            1 para binário, 
                                            2 para octal e
                                            3 para hexadecimal.'''


num = int(input('Digite um número inteiro qualquer: '))


print(f'\nVocê escolheu o número {num}.')
print('\nDigite [1] para converter para o sistema Binário.')
print('Digite [2] para converter para o sistema Octal.')
print('Digite [3] para converter para o sistema Hexadecimal.')


base_conversao = int(input('\nInforme aqui sua resposta: '))


if base_conversao == 1:
    print(f'{num} convertido para Binário é: {bin(num)[2:]}')
elif base_conversao == 2:
    print(f'{num} convertido para Octal é: {oct(num)[2:]}')
elif base_conversao == 3:
    print(f'{num} convertido para Hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção Inválida!!!')

