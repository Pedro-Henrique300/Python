'''Crie um programa que faça o computador jogar Jokenpô com você.'''



from random import randint
from time import sleep

print('''
    Suas opções:

    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    ''')
 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('\nQual a sua jogada? '))



print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')



print('-=-' * 9)
print(f'Computador jogou: {itens[computador]}')
print(f'jogador jogou: {itens[jogador]}')
print('-=-' * 9)



if computador == 0:
    if jogador == 0:
        print('\nEmpate')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Eu Venci!')
    else:
        print('JOGADA INVÁLIDA!')
            
elif computador == 1:
    if jogador == 0:
        print('Eu Venci!')
    elif jogador == 1:
        print('\nEmpate')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Eu Venci!')
    elif jogador == 2:
        print('\nEmpate')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!')