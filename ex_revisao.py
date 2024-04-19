"""
#Luca Gabriel Pace Girardi - RA 2023.029.373.57

#Deixei os exercícios comentados com """""" para facilitar, é só tirar para executar cada um deles indiviualmente
#Exercicio 1
horas = float(input("Digite o número de horas: "))
cobranca = horas * 5

if cobranca <= 35:
    print(cobranca)
else:
    print("35")

#Exercício 2

bloco = int(input("Digite o bloco: "))
if bloco >= 1 and bloco <= 10:
    print("Sr. José")
elif bloco>10 and bloco<=20:
    print("Sr. Hamilton")
else:
    print("Digite um número válido de blocos")

#Exercício 3
notas=[]
for i in range(3):
    nota = float(input(f"Digite sua nota {i+1} "))
    notas.append(nota)
nota_final = notas[0]*0.4+notas[1]*0.4+notas[2]*0.2

if nota_final>= 9:
    print("A")
elif nota_final>= 7.5:
    print("B")
elif nota_final>= 6:
    print ("c")
elif nota_final>= 4.5:
    print("D")
else:
    print("E")

#Exercício 4
clientes = ["Mário", "Flávio", "Eduardo", "Ana Luiza", "Luca"]
compras_cliente=[]
maior_100 = []
menor_50 = []
for i in range(5):
    quanto_comprou = float(input(f"Quanto {clientes[i]} comprou?"))
    compras_cliente.append(quanto_comprou)
    if quanto_comprou>100:
        maior_100.append(quanto_comprou)
    elif quanto_comprou<50:
        menor_50.append(quanto_comprou)
    
        
soma = sum(compras_cliente)
media = soma/len(compras_cliente)

print(f"O valor total comprado foi {soma}")
print(f"A média foi de {media}")
print(f"O número de clientes que comprou mais que 100 foi de {len(maior_100)}")
print(f"O número de clientes que comprou menos de 50 foi de {len(menor_50)}")

#Exercício 5
for i in range(4):
    numero = int(input(f"Digite o número {i+1}°"))
    if numero % 2 == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é ímpar")
    if numero % 3 == 0:
        print("O número é múltiplo de 3")
    else:
        print("O número não é múltiplo de 3")
    if numero>0:
        print("O número é positivo")
    elif numero < 0:
        print("O número é negativo")


#Exercício 6
numero = int(input("Digite um número inteiro"))
for i in range(10):
    print(f"{numero}x{i+1} = {numero*(i+1)}")

#Exercício 7

lista = []
pares = []
for i in range(10):
    digitado = int(input(f"Digite seu {i+1}° número inteiro "))
    lista.append(digitado)
    if digitado % 2 == 0:
        pares.append(digitado)
print(f"Esses são os números pares: {pares}")

print(f"Há {len(pares)} números pares na lista")


#Exercício 8

lista_8 = []
 
for i in range(10):
    digitado_8 = int(input(f"Digite seu {i+1}° número inteiro "))
    lista_8.append(digitado_8)
print(f"O maior número é {max(lista_8)}")
print(f"O menor número é {min(lista_8)}")


#Exercício 9

idade = []
menoridade=[]
digitado_9=int(input("Digite sua idade: "))
if digitado_9 >= 0:

    while digitado_9 >= 0:
        idade.append(digitado_9)
        if digitado_9 < 18:
           menoridade.append(digitado_9)
        
        digitado_9=int(input("Digite sua idade: "))
print(f"O número de menores é de {len(menoridade)}")
print(f"A média de idades é {sum(idade)/len(idade)}")

"""
#Exercício 10

lista_10 = []
l_div3 = []
l_div4 = []

for i in range(10):
    entrada = int(input(f"Digite o {i+1}° número inteiro"))

    if entrada % 3 == 0:
        l_div3.append(entrada)
    elif entrada % 4 == 0:
        l_div4.append(entrada)

print (f"Os números digitados foram {lista_10}")
print(f"Os números divíseis por 4 digitados foram {l_div4}")
print(f"Os números digitados díviseis por 3 são {l_div3}")