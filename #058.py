# elhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0,10)
print('sou o seu computador... acabei de pensar num numero entre 0 e 10.')
print('sera que voce vai adivinhar qual foi?')
acertou = False # false porque? porque ainda nao acertamos
palpite = 0
while not acertou:
    jogador = int(input('qual o seu palpite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('suba mais...')
        elif jogador > computador:
            print('desce um bocado...')

print('acertou com {} tentativas'.format(palpite))