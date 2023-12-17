'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


opção = 'S'
soma = cont = menor = maior = 0

while opção != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    opção = str(input('\nQuer continuar ? [S/N] ')).strip().upper()[0]

media = soma / cont

print(f'\nA média entre esses números é: {media}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')