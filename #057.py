#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('qual o seu sexo? (M/F)')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input(' dados inválidos. por favor digite o seu sexo: ')).strip().upper()[0]
print('sexo {} registado com sucesso'.format(sexo))