#Sorteio aleatório
import random
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O aluno escolhido é {}'.format(escolhido))