#verificador de idade
Idade=int(input("Digite sua idade : "))
if Idade <= 13:
    print("Você é criança")
elif Idade <= 17:
    print("Você é adoslecente")
elif  Idade <= 59:
    print(" Você é adulto")
else: 
 print("Você é idoso")