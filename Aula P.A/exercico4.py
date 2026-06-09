#escrever um programa que solicita um valor de saque de dinheiro para o usuario e 
# informe quais notas serao ultilizada


valor = int (input("Digite um valor: "))

qtd100 = 0 
while valor >= 100: 
    valor -=100
    qtd100 +=1

qtd50 = 0
while valor >= 50:
    valor -= 50
    qtd50 +=1

qtd20 = 0
while valor >= 20:
    valor -= 20
    qtd20 +=1

qtd10 = 0
while valor >= 10:
    valor -= 10
    qtd10 +=10

print (f"Notas de 100: {qtd100}")
print (f"Notas de 50: {qtd50}")
print (f"Notas de 20: {qtd20}")
print (f"Notas de 10: {qtd10}")

