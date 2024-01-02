'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''


soma = produtos_caros = menor = cont = 0
nome_barato = ''

while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip()
    preço_produto = float(input('Informe o preço do produto: '))
    opção = ' '
    cont += 1
    while opção not in 'sn':
        opção = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    
    soma += preço_produto

    if preço_produto > 1000:
        produtos_caros += 1

    if cont == 1:
        menor = preço_produto
        nome_barato = nome_produto
    else:
        if preço_produto < menor:
            menor = preço_produto
            nome_barato = nome_produto

    if opção == 'n':
        break

print(f'\nO total de gastos foi de R${soma:.2f}.\n{produtos_caros} custam mais de R$1000.\nO produto mais barato custa foi {nome_barato}, que custa R${menor:.2f}.')