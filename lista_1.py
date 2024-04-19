#Exercício 1
"""
vetor =[]
numero = 1

while numero>0:
    numero = int(input("Digite um número inteiro positivo"))
    vetor.append(numero)

maior = max(vetor)
menor = min(vetor)
print(f"O maior é {maior} e o menor é {menor}")
"""
#Exercicio 2

vetor =[]
numero = 1
positivo = []

while numero>0:
    numero = int(input("Digite um número inteiro"))
    vetor.append(numero)
    if numero > 0:
        positivo.append(numero)
soma_positivo = sum(positivo)
print(f"A soma dos positivos é {soma_positivo} e os numeros que foram somados foram {positivo}" )



    



