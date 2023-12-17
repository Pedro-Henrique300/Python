'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''


from random import randint

print('-=-'*23)
print('Eu vou pensar em um número de 0 a 10. E você vai ter que adivinhar...')
print('-=-'*23)

computador = randint(0, 10)
jogador = int(input('\nDigite um palpite: '))
palpites = 0

while jogador != computador:
    print(f'\nVocê errou! Tente Novamente...')
    if jogador < computador:
        print('O número que pensei é maior.')
    else:
        print('O número que pensei é menor.')
    jogador = int(input('\nDigite um palpite: '))
    palpites += 1

print(f'\nParabéns!!! Você acertou, foram precisos {palpites+1} palpites!')