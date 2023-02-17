# crie um programa que leia o ano de nascimento de sete pessoas.
# no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
actual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range (1,8):
    d_nasc = int(input('qual o ano de nasicmento da {}ª pessoa? '.format(pessoas)))
    idade = actual - d_nasc
    if idade < 18:
        total_menor +=1
    elif idade > 18:
        total_maior += 1
print(' existem {} pessoas menor de idade'.format(total_menor))
print('existem {} pessoas maior de idade'.format(total_maior))
