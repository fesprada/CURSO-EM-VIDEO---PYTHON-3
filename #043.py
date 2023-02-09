# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calucle o IMC e mostre seu status, de caordo com a tabela abaixo:
# IMC abaixo de 18,5: abaixo do peso;
# entre 18,5 e 25: peso ideal;
# entre 25 ate 30: sobrepeso
# entre 30 a 40: obesidade
# acima de 40: obesidade morbida

peso = float(input('qual o seu peso?(kg) '))
altura = float(input('qual a sua altura?(m) '))
IMC = (peso) / (altura ** 2)
print('o seu IMC é de {}'.format(IMC))
if IMC < 18.5:
    print('encontra-se abaixo do peso ideal')
elif 25 > IMC > 18.5:
    print('tem o peso ideal')
elif 25 < IMC < 30:
    print('tem excesso de peso')
elif 30 < IMC < 40:
    print(' é obeso ')
else:
    print('obesidade morbida')
