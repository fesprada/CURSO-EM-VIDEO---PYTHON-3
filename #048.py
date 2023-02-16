#faça um programa que calculer a soma entre todos os numeros impares que são multiplos de tres e que se encontra no intervalo de 1 até 500.

soma = 0
cont = 0
for n in range (1,501,2):
    if n%3 == 0:
        soma += n
        cont += 1
print('a soma de todos os {} valores solicitados é {}.'.format(cont,soma))