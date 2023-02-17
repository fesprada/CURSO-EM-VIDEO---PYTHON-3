# faça um programa que leia um  nº inteiro e diga se ele é primo ou não.

num = int(input('digite um nunemro inteiro: '))
total = 0 # total de vezes que o num escolhido é divisivel
for c in range(1, num +1): # numero primo é apena divisil por >> "1" e por ele proprio >> "num +1", vai ler de 1 a num+1, ou seja, nunca lê o ultimo por isso temos que somar mais um ao numero que escolhemos.
    if num %c == 0:
        total += 1
print('o numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print(' é primo')
else:
    print('não é primo')
