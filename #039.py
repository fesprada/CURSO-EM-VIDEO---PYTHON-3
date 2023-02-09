# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
actual = date.today().year
nasc= int(input(' qual o ano de nascimento? '))
idade = actual - nasc
print ('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, actual))
if idade == 18:
    print('voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print(' ainda faltam {} anos para se alistar'.format(saldo))
    ano= actual + saldo
    print('seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('voce ja deveria ter-se alistado há {} anos.'.format(saldo))
    ano = actual - saldo
    print('seu alistamento deveria ter sido no ano de {}'.format(ano))
