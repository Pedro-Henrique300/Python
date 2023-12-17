'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('\nSexo Invalido!!! Tente Novamente')
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
