# Conversão de valor:
milhas=float(input("Digite um número: "))
f= (milhas * 1.609340)
if milhas :
 print("o valor em milhas é ",format(f))
polegadas=float(input("Digite um número: "))
p= (polegadas * 2.54)
if polegadas: 
 print("O valor em polegadas é: ",format(p))
pés=float(input("Digite um número: "))
pé= (pés * 30.48)
if pés: 
 print("O valor em centimetros é: ",format(pé))
centimetro=float(input("Digite um número: "))
c= (centimetro / 100)
if centimetro:
 print("O Valor em centimetros é: ",format(c))
metros=float(input("Digite um número: "))
m= (metros / 100)
if metros:
 print("O valor em metros é:",format(m))
quilometros=float(input("Digite um número: "))
q= (quilometros /  1000)
if quilometros:
 print("O valor em quilometros é: ",format(q))
else:
 print("Erro !")
