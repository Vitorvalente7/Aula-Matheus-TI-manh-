# Verificação de triangulo e tipo de triangulo !!
área=float(input("Digite a área do triangulo: "))
base=float(input("Digite a base do triangulo: "))
c=float(input("Digite a altura do triangulo: "))
if (área < base + c) and (base < área + c) and (c < área + base) :
    print(" É possivel formar um triangulo !")
    if  (área == base) and (c == área) :
      print("Equilatero")
    elif área != base != c != área :
      print(" Escaleno ! ")
    else:
      print(" Iósceles ! ")
else:
 print("Não é possivel formar um triangulo !")
