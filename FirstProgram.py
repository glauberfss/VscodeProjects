from random import randint
from time import sleep

def processar_informação(jogador, computador, itens):
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    if computador == 0:
        if jogador == 0:
            print('\033[32mEMPATE.\033[m')
        elif jogador == 1:
            print('\033[32mJogador Vence.\033[m')
        elif jogador == 2:
            print('\033[32mComputador Vence\033[m.')
        else:
            print('\033[33mJogada Inválida\033[m.')

    if computador == 1:
        if jogador == 0:
            print('\033[32mComputador Vence.\033[m')
        elif jogador == 1:
            print('\033[32mEMPATE.\033[m')
        elif jogador == 2:
            print('\033[32mJogador Vence.\033[m')
        else:
            print('\033[33mJogada Inválida.\033[m')

    if computador == 2:
        if jogador == 0:
            print('\033[32mJogador Vence.\033[m')
        elif jogador == 1:
            print('\033[32mComputador Vence.\033[m')
        elif jogador == 2:
            print('\033[32mEMPATE.\033[m')
        else:
            print('\033[33mJogada Inválida.\033[m')


def start():
    itens = ['pedra', 'papel', 'tesoura']
    print('''Suas opções: 
    [0] - PEDRA
    [1] - PAPEL
    [2] - TESOURA''')
    while True:
        computador = randint(0,2)
        jogador = int(input('Qual é a sua jogada? > '))
        print('JO')
        sleep(1)
        print('KE')
        sleep(1)
        print('PÔ')
        sleep(1)
        print('=' * 15)
        
        processar_informação(jogador, computador, itens)
        print('=' * 15)
        resultado = ''
        resultado = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resultado == 'N':
            print('Encerrando...')
            print('Até mais!')
            sleep(1)
            break 
        

if __name__ == '__main__':
    start()