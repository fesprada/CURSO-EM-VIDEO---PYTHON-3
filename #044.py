#elabore um programa que calculer o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10>% desconto;
# a vista no cartao: 5% desconto;
# em até 2x no cartao: preço formal;
# em 3x ou mais no cartao: 20% juros;

print('{:=^50}'.format('LOJAS GUANABARA'))
preço = float(input('qual o preço do artigo? '))
print(''' FORMAS DE PAGAMENTO
[1] DINHEIRO / CHEQUE
[2] CARTÃO
[3} ATÉ 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')
opçao = int(input('qual a sua opçao de pagamento? '))
if opçao == 1:
    total = preço - (preço * 10/100)
    desc = (10/100) * preço
    print('o preço a pagar será de {}€, tendo ja cerca de 10 por cento de desconto: {}€'.format(total,desc))
elif opçao == 2:
    total = preço - (preço * 5/100)
    desc= (5/100) * preço
    print('o preço a pagar será de {}€, tendo já deesconto no valor de {}€'.format(total,desc))
elif opçao ==3:
    total = preço
    valor_parc = total/2
    print('o valor do artigo a pagar será de {}€, sendo pago em 2 parcelas, no valor de {:.2f}€ cada uma.'.format(total,valor_parc))
elif opçao == 4:
    total = preço + (preço * 20/100)
    parc = int(input('quantas parcelas?'))
    valor_parc = total / parc
    print('o valor total a pagar será de {}€ em cerca de {} parcelas. cada parcela sera de {}€'.format(total,parc,valor_parc,))


