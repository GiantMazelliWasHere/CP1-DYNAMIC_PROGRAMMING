cresente = [0,1,2,3,4,5,6,7,8,9]
decresente = [9,8,7,6,5,4,3,2,1,0]
nao_ordenados = [5,3,2,4,7,1,0,6,8,9]

def selection_sort(vetor):
    quantidade_torcas = 0
    for i in range(len(vetor)):
        menor = i
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
                quantidade_torcas += 1
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
    print("Quantidade de trocas: ", quantidade_torcas)
    print(vetor, "\n")

print('Vetor Crescente:')
print(cresente)
selection_sort(cresente)

print('Vetor Decrescente:')
print(decresente)
selection_sort(decresente)

print('Vetor Não Ordenado:')
print(nao_ordenados)
selection_sort(nao_ordenados)