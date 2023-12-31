'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
    No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''


maior_idade = qtd_homem = qtd_mulher_menor = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = " "
    while sexo not in 'fm':
        sexo = str(input("Digite o sexo da pessoa [F/M]: ")).strip().lower()[0]
    if idade >= 18:
        maior_idade += 1
    if idade < 20 and sexo == 'f':
        qtd_mulher_menor += 1
    if sexo == 'm':
        qtd_homem += 1

    opção = " "
    while opção not in 'sn':
        opção = str(input("\nDeseja continuar? [S/N]: ")).strip().lower()[0]
    if opção == 'n':
        break

print(f'\nCom base na analise: \n{maior_idade} pessoas são maiores de idade. \nForam cadastrados {qtd_homem} homens. \nEntre as mulheres, {qtd_mulher_menor} possuem idade menor que 20 anos.')