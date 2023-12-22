''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
    O programa será interrompido quando o número solicitado for negativo. '''


while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-'*20)
    if num < 0:
        break
    for i in range(11):
        print(f'{num} X {i} = {num*i:2}')
    print('-'*20)

print('O programa foi encerrado, volte sempre.')