#calculadora de IMC
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
IMC= peso/(altura*altura)
if IMC <18.5:
    print("Magreza !")
elif IMC <=24.9:
    print("Normal !")
elif IMC <=30:
    print("Sobrepeso !")
elif IMC <=40:
    print("Obesidade !")

