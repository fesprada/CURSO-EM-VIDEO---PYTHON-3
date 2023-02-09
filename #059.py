# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input('digite um valor: '))
valor2 = int(input('digite outro valor: '))
opçao = 0
while opçao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa ''')
    opçao = int(input('qual a sua opção? 1-5: '))
    if opçao == 1:
        soma = valor1 + valor2
        print('a soma entre {} e {} é de, {}'.format(valor1,valor2,soma))
    elif opçao == 2:
        produto = valor1 * valor2
        print('o produto entre {} e {} é de, {}'.format(valor1,valor2,produto))
    elif opçao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('entre {} e {}, o maior valor é {}'.format(valor1,valor2,maior))
    elif opçao == 4:
        print('seleccione novos valores: ')
        valor1 = int(input('primeiro valor:'))
        valor2 = int(input('segundo valor:'))
    elif opçao == 5:
        print('finalzando o programa...')
    else:
        print('opçao invalida. tente novamente')
    print('='*30)
print('fim do programa')


