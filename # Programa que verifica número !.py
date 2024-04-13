# Programa que verifica número
número= int(input("Digite um número: "))
resultado=número % 2
if resultado ==0:
    print("Este número é positivo e par !",format(número))
else:
    print("Este número é positivo e ímpar !",format(número))
if número % 3 == 0 :
    print("Este número é multiplo de  três !")
elif número ==0:
    print("Este número é zero !")
elif número < 0 and número % 2 == 1 :
    print("Este número é negativo e ímpar !")
else:
    print("O número não é multiplo de três ! ")