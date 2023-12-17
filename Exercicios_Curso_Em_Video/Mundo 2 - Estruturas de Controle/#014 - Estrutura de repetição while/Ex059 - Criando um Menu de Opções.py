'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''


valor_1 = int(input('Digite o 1º valor: '))
valor_2 = int(input('Digite o 2º valor: '))
opcao = 0

while True:
    print('-=--=-MENU-=--=-')
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')

    opcao = int(input('\nQual é sua opção? '))

    if opcao == 1:
        soma = valor_1 + valor_2
        print(f'\nA soma entre {valor_1} e {valor_2} é igual a: {soma}')
    elif opcao == 2:
        mult = valor_1 * valor_2
        print(f'\nA multiplicação entre {valor_1} e {valor_2} é igual a: {mult}')
    elif opcao == 3:
        maior = valor_1
        if valor_2 > maior:
            maior = valor_2
            print(f'\nO maior valor é: {maior}')
        elif valor_1 == valor_2:
            print('\nNão existe maior, os valores são iguais!')
    elif opcao == 4:
        print('\nCerto, reescreva os valores.')
        valor_1 = int(input('Digite o 1º valor: '))
        valor_2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        break
    else:
        print('\nOpção Invalida!!!')

