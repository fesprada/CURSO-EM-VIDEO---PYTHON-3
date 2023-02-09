# Refaça o exercicio #035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formadpo:
# equilatero: todos os lados sao iguais;
# isosceles: 2 lados iguais, 1  diferente;
# escaleno: todos os lados diferentes.

# CONDIÇÃO EXISTENCIA DE UM TRIANGULO
# |b-c| < a < |b+c|
# |a-c| < b < |a+c|
# |a-b| < c < |a+b|
# if R1 < R2 + R3 and R2 < R3 + R1 and R3 < R1 + R2:
# print(' os segmentos acima formam um triangulo')
# else: print(' os segmetnos não podem formar um triangulo')'

r1 = float(input('medida do primeiro segmento: '))
r2 = float(input('medida do segundo segmento: '))
r3 = float(input('medida do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1+r2:
    print('os segmentos acima podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('equilatero')
    elif r1 != r2 != r3 != r1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('os segmentos não podem formar um triangulo')
    