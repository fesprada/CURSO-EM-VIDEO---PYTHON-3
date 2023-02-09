# crie um programa que leia duas notas de um aluno e calcule a sua ,édia, mpstrando uma mensagem no final, de acordo com amédia atingida:
# média abaixo de 5.0: REPROVADO;
# média de 5.0 e 6.9: RECUPERAÇÃO;
# média de 7.0 ou superior: APROVADO.

n1=float(input('digita a 1a nota:  '))
n2=float(input('digite a 2a nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('sua média foi de {}, está REPROVADO.'.format(média))
elif 5 <= média < 6.9:
    print('sua média foi de {}, está em fase de RECUPERAÇÃO.'.format(média))
else:            # -------»»»»» ou elif média >= 7:
    print('sua média foi {}, está APROVADO. PARABÉNS!'.format(média))
