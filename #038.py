# Escreva um programa que leia dois números inteiros e compare-os.
# Mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1= int(input('escolha um numero inteiro '))
num2= int(input(' escolha outro numero inteiro '))
if num1 < num2:
    print('segundo valor é maior')
elif num1 > num2:
    print(' primeiro valor é maior')
else:
    print('os dois valores são iguais')


