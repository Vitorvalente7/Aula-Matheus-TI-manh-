# Verificação de triangulo e tipo de triangulo !!
area=float(input("Digite a area do triangulo: "))
base=float(input("Digite a base do triangulo: "))
c=float(input("Digite a altura do triangulo: "))
if (area < base + c) and (base < area + c) and (c < area + base) :
    print(" É possivel formar um triangulo !")
    if  (area == base) and (c == area) :
      print("Equilatero")
    elif area != base != c != area :
      print(" Escaleno ! ")
    else:
      print(" Iósceles ! ")
else:
 print("Não é possivel formar um triangulo !")