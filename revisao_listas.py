"""AC na sexta-feira"""

"""Listas é o que o professor chama para vetores. Legal lembrar dos operadores de vetores,
como vetor.append.

Voce quer mostrar do primeiro elemento ao quarto do vetor: print(vetor[0:3]) -- voce usa :
len(vetor) - para saber o tamanho, e ele mostra 6 elementos por ex de um vetor que vai do indice 0 ao 5
vetor.append
vetor. insert (numero, posição)
vetor.pop (remove o último elemento)
vetor.remove(posição) - remove na posição 

funções: 
sum(vetor)
max(vetor)
min(vetor)
for i in lista[i]
"""
vetor = []
for i in range(5):
    numero = float(input("Digite um numero"))
    vetor.append(numero)

print(vetor)

