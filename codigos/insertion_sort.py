cresente = [0,1,2,3,4,5,6,7,8,9]
decresente = [9,8,7,6,5,4,3,2,1,0]
nao_ordenados = [5,3,2,4,7,1,0,6,8,9]

def insertion_sort(vetor):
    length = len(vetor)
    quantidade_trocas = 0
    for i in range(1, length):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and chave < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
            quantidade_trocas += 1
        vetor[j + 1] = chave
    print("Quantidade de trocas: ", quantidade_trocas)
    print(vetor, "\n")

print('Vetor Crescente:')
print(cresente)    
insertion_sort(cresente)

print('Vetor Decrescente:')
print(decresente)
insertion_sort(decresente)

print('Vetor Não Ordenado:')
print(nao_ordenados)
insertion_sort(nao_ordenados)