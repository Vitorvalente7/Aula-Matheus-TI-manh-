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
 print("O valor em centímetros é: ",format(pé))
centímetro=float(input("Digite um número: "))
c= (centímetro / 100)
if centímetro:
 print("O Valor em centímetros é: ",format(c))
metros=float(input("Digite um número: "))
m= (metros / 100)
if metros:
 print("O valor em metros é:",format(m))
quilômetro=float(input("Digite um número: "))
q= quilômetro /  1000
if quilômetro :
 print("O valor em quilômetro é: ",format(q))
else:
 print("Erro !")
