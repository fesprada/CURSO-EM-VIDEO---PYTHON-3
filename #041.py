# a confederação naciopnal de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JÚNIOR
# até 25 anos: SÉNIOR
# acima de 25 anos: MASTER

from datetime import date
actual = date.today().year
nasc = int(input('qual o seu ano de nascimento? '))
idade = actual - nasc
print('o atleta, nascendo no ano de {}, tem cerca de {} anos'.format(nasc, idade))
if idade <= 9:
    print('o atleta tendo {} anos, pertence a categoria MIRIM'.format(idade))
elif idade <= 14:
    print('CALSSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('classificaçai: JÚNIOR')
elif idade <= 25:
    print('classificação: SÉNIOR')
else: # ------>>>>> OU elif idade > 25:
    print('classificação: MASTER')
