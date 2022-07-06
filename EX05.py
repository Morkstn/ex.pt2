#Analise do nome
nome = str(input('Digite um nome:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúscula é: {}'.format(nome.lower()))
print('Seu nome tem ao todo é: {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))