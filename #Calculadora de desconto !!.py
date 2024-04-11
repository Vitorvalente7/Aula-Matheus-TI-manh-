#Calculadora de desconto !!
preco=float(input("digite o preço: "))
desconto=float(input("Digite o valor do desconto: "))
f= preco - (preco * desconto / 100)
print(" O desconto é R$ :",format (f))
