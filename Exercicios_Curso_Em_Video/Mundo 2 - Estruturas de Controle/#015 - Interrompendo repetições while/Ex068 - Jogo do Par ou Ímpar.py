'''  Faça um programa que jogue par ou ímpar com o computador. 
    O jogo só será interrompido quando o jogador perder, 
    mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
 '''


from random import randint

print('-'*20)
print('JOGO DO PAR OU ÍMPAR')
print('-'*20)

soma = vitorias = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Escolha um número: '))
    soma = computador + jogador
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()[0]
    print(f'\nVocê jogou {jogador} e o computador jogou {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')

    if opção == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif opção == 'I':
        if soma % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('\nVamos jogar novamente....\n')

print(f'\nO jogo acabou com {vitorias} vitórias do jogador!')
