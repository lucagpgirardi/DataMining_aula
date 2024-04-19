#Só pra lembrar de alguma coisa

numero1 = float(input("Digite o primeiro número da operação"))
operação = input("Digite a operação desejada, como +, -,*, /, ^ ")
numero2 = float(input("Digite o segundo número da operação"))
resultado = 0

if operação =="+":
    resultado = numero1 + numero2
elif operação == "-":
    resultado = numero1 - numero2
elif operação == "*":
    resultado = numero1 * numero2
elif operação == "/":
    resultado = numero1 / numero2


else:
    print("Operação inválida")

print(resultado)
