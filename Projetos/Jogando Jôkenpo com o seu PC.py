#!/usr/bin/env python
# coding: utf-8

# In[18]:


from random import randint
from time import sleep

# cores que utilizei
cores = {
    'ciano':'\033[1;36m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'limpa':'\033[m',
}

# pedindo ao usuario informar seu nome
nome_jogador = str(input('\nQual seu nome? ')).strip()
print(f'{cores["ciano"]}\nOk {nome_jogador}! Tente vencer de mim O.o\n{cores["limpa"]}')

rodadas = 0
pontos_jogador = 0
pontos_computador = 0
empates = 0

while True:
    # caso um dos dois atinja 10 pontos o laço encerra, mostrando o vencedor
    if pontos_computador >= 10 or pontos_jogador >= 10:
        print('\nO duelo acabou...pois temos um vencedor: ', end='')
        if pontos_jogador > pontos_computador:
            print(f'Parabéns {cores["verde"]}{nome_jogador}{cores["limpa"]} você venceu esse duelo!')
        elif pontos_computador > pontos_jogador:
            print(f'O {cores["ciano"]}computador{cores["limpa"]} venceu esse duelo!')
        break
        
    print(f'''-=--=--=--=- PLACAR -=--=--=--=-
    {nome_jogador}: {pontos_jogador}  computador: {pontos_computador}''')
    print(f'\n{rodadas+1}ª Rodada.\n')
    
    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    ''')
    
    computador = randint(0, 2) # o computador escolhe um número
    itens = ('Pedra', 'Papel', 'Tesoura')
    
    # caso o jogador informe uma opção inválida ou tecle Enter sem escolher uma opção, é informado do erro e o jogo continua
    try:
        jogador = int(input('\nQual a sua jogada? ')) # o jogador escolhe um número
    except ValueError:
        print(f'\n{cores["vermelho"]}Ops! Você teclou Enter sem escolher uma opção!{cores["limpa"]}\n')
        continue
    if jogador not in [0, 1, 2]:
        print(f'\n{cores["vermelho"]}Opção inválida! Escolha entre 0, 1 ou 2.{cores["limpa"]}\n')
        continue
        
        
    print(f'{cores["ciano"]}\nJÔ')
    sleep(1)
    print(f'{cores["verde"]}KEN')
    sleep(1)
    print(f'{cores["verde"]}P{cores["ciano"]}O{cores["limpa"]}!!!')
    
    # mostrando oque cada um escolheu
    print('-=-' * 9)
    print(f'{cores["ciano"]}Computador jogou: {itens[computador]}')
    print(f'{cores["verde"]}{nome_jogador} jogou: {itens[jogador]}{cores["limpa"]}')
    print('-=-' * 9)
    
    if computador == jogador:
        print('\nEmpate\n') # em caso de empate
        empates += 1
    elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
        print(f'\n{cores["ciano"]}Eu Venci!{cores["limpa"]}\n') # em caso de vitória do computador
        pontos_computador += 1
    else:
        print(f'\n{cores["verde"]}{nome_jogador} Venceu!{cores["limpa"]}\n') # caso de vitória do jogador
        pontos_jogador += 1
    
    # encrementa a rodada
    rodadas += 1

    
# apresentando os resultados finais
print(f'''\n-=--=--=--=- Resultados finais -=--=--=--=-
Empates: {empates}
{nome_jogador}: {pontos_jogador}
Computador: {pontos_computador}''')

