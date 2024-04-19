#Luca Girardi - 202302937357 e Giovanni Bruno - 202301097614
#Exercicio 1

vetor =[]
par = []
impar =[]

for i in range(10):
    numero = int(input("Digite um número inteiro "))
    vetor.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"A lista geral é {vetor}, a lista de pares é {par} e a lista de ímpares é {impar}")

#Exercicio 2
lista1 = [2,5,7,3,6,4,6,8,87,10]
lista2 = [1,7,4,6,4,7,4,7,4,7]
lista3 = []
for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    
else:
    print("erro")

print(lista3)

#Exercício 3
media_vetor =[]
aprovados =[]
for i in range(10):
    nome = input("Digite seu nome")
    nota1 = float(input("Digite sua primeira nota"))
    nota2 = float(input("Digite sua segunda nota"))
    nota3 = float(input("Digite sua terceira nota"))
    media = (nota1+nota2+nota3)/3
    media_vetor.append(media)

for i in range(len(media_vetor)):
    if media_vetor[i] >=7:
        aprovados.append(media_vetor[i])

print(len(aprovados))

#Exercício 4

numeros_input = float(input("Digite um número"))
numeros=[]
acima=[]
abaixo=[]
while numeros_input != -1:
    numeros.append(numeros_input)
    numeros_input = float(input("Digite um número"))


media = sum(numeros)/len(numeros)
for i in range(len(numeros)):
    if numeros[i]> media:
        acima.append(numeros[1])
    elif numeros[i]< media:
        abaixo.append(numeros[i])

print(f"Temos {len(acima)} números acima da média e {len(abaixo)} abaixo")


print(f"A soma dos números é {sum(numeros)}")
print(f"A média é {media}")










