#Conversor de real para dolar
real = float(input('Quanto dinheiro você têm na carteira R$?'))
dolar = real / 5.40
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))