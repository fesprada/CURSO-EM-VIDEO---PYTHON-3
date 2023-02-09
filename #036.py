# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('valor da casa: (em euros) '))
salário = float (input('qual o seu salário? '))
anos = int(input('em quantos anos pretende pagar? '))
prestação_mensal = valor_casa/ (12*anos)
minimo = salário * 30/100
print('para pagar uma casa no valor de {} € em {} anos'.format(valor_casa, anos), end='')
print(' a prestação será de {} €'.format(prestação_mensal))

if prestação_mensal <= minimo:
    print(' emprestimo aprovado.')
else:
    print('o empréstimo não foi aprovado')

