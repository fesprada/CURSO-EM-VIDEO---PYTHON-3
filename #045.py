# JOGO: PEDRA, PAPEL, TESOURA
#crie um programa que faça o computador jogar consigo.

from random import randint
print('{:=^60}'.format(' PEDRA - PAPEL - TESOURA '))
itens =['pedra','papel','tesoura']
computador = randint(0,2)
print(''' suas opções:
[0] Pedra
[1] Papel
[2] Tesoura ''')
jogador = int(input('qual a sua opção? '))
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}.'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('empate!')
    elif jogador == 1:
        print('ganhou')
    elif jogador == 2:
        print('perdeu')
    else:
        print('jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('perdeu')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('ganhou')
    else:
        print('jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('ganhou')
    elif jogador == 1:
        print('perdeu')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada inválida')
