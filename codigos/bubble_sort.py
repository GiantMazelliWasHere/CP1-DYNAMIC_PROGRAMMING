cresente = [0,1,2,3,4,5,6,7,8,9]
decresente = [9,8,7,6,5,4,3,2,1,0]
nao_ordenados = [5,3,2,4,7,1,0,6,8,9]

def bubble_sort(vetor):
    length = len(vetor)
    quantidade_trocas = 0
    for i in range(length):
        for j in range(0, length - i -1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                quantidade_trocas += 1
    print("Quantidade de trocas: ", quantidade_trocas)          
    print(vetor, "\n")
    
print('Vetor Crescente:')
print(cresente)
bubble_sort(cresente)

print('Vetor Decrescente:')
print(decresente)
bubble_sort(decresente)

print('Vetor Não Ordenado:')
print(nao_ordenados)
bubble_sort(nao_ordenados)