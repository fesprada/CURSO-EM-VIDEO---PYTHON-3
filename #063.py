# escreva um programa que leia um numero N inteiro qualquer e mostre na tela
# os N números elementos de uma sequencia fibonacci

n = int(input('quantos elementos quer ver da sequencia fibonacci? '))
t1 = 0
t2 = 1
print('{} » {}'.format(t1,t2),end='')
cont = 3
while n >= cont:
    t3 = t1 + t2
    print(' » {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' » fim')