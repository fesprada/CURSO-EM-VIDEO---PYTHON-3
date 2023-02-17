# crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# ex.: apos a sopa / sacada da casa / a torre da permuta / o lobo ama o bolo / anotaram a data da maratona.

frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split() # separar as palavras, ex: ['Curso', 'em', 'Video']
junto = ''.join(palavras) # vai juntar as palavras para eliminar os espaços, ex: 'CURSOEMVIDEO'
inverso = junto[::-1] # vai ler a palavra do principio ao fim, em ordem inversa
print ('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('temos um palindromo')
else:
    print('não é palindromo')