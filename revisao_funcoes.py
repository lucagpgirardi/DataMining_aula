#Para definir uma função, usamos def
#Usamos return para que seja atribuido o valor final àquela função
#Para chamar a função, usamos função(argumento) como qualquer outra nativa do python

#Exemplo
def interpolar (lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return(lista3)

alunos1 = []
alunos2 = []
for i in range(3):
    alunos_A = input("Digite seu nome na turma A")
    alunos1.append(alunos_A)
    alunos_b = input("Digite seu nome na turma B")
    alunos2.append(alunos_b)

print(interpolar(alunos1, alunos2))



