'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''


fatorial = 1
num = int(input('Digite um número para saber seu fatorial: '))
c = num

print(f'Calculando {num}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1

print(f'{fatorial}')