# refaça o desafio #009, mostrando a tabuada de um numero que o usuario escolhe.
#só que agora utilizando um laço FOR.
from time import sleep
num = int(input('escolha um numero para obter a sua tabuada ate 10: '))
for tab in range (1,11):
    print('{} x {} = {}'.format(num, tab, num * tab))
    sleep(1)
    
    #o <import sleep> foi um acrescento 