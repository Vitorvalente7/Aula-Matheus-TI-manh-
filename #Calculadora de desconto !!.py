#Calculadora de desconto !!
preço=float(input("digite o preço: "))
desconto=float(input("Digite o valor do desconto: "))
f= preço - (preço * desconto / 100)
print(" O desconto é R$ :",format (f))
