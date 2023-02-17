#deesnvola um programa que leia o primeiro termo e a razão de uma PA(prograssao aritmetica). 
# no final, mostre os 10 primeiros termos dessa progressão.

# primeiro termo: 0
# razão: 2
# 0 > 2 > 4 > 6 > 8 > 10 > 12 > 14 > 16 > 18 > Acabou!

primeiro = int(input('primeiro termo? '))
razao = int(input('razao? '))
decimo = primeiro + (10-1) * razao # formula progressao aritmetica
for c in range (primeiro, decimo + razao, razao):
    print('{} > '.format(c), end='')
print('acabou')