from random import randint
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA
''', end='')
jogadas = int(input('Qual sua jogada?'))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('*' * 20)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[jogadas]))
print('*' * 20)
if computador == 0: # pedra
    if jogadas == 0:
        print('EMPATE')
    elif jogadas == 1:
        print('JOGADOR VENCEU')
    elif jogadas == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')
elif computador == 1: # papel
    if jogadas == 0:
        print('COMPUTADOR GANHOU')
    elif jogadas == 1:
        print('EMPATE')
    elif jogadas == 2:
        print('JOGADOR VENCEU')
    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')
elif computador == 2:
    if jogadas == 0:
        print('JOGADOR VENCEU')
    elif jogadas == 1:
        print('COMPUTADOR VENCEU')
    elif jogadas == 2:
        print('EMPATE')
    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')
