'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

print('Série de Fibonacci\n')

termos = int(input('Quantos termos serão apresentados? '))
ant2 = 0
ant1 = 1
i = 3

print(ant2, end=' -> ')
print(ant1, end=' -> ')

while i <= termos:
    atual = ant1 + ant2
    print(atual, end=' -> ')
    ant2 = ant1
    ant1 = atual
    i += 1
print('ACABOU')