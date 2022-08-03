import json
import numpy as np

def calcMes (arquivo): #funcao para realizar os calculos do mes desejados
    arr = np.zeros(len(arquivo)) #cria um vetor do tamanho dos dias do arquivo
    for i in range(len(arquivo)):
        arr[i] = arquivo[i]["valor"] #anexa no vetor gerado o valor correspondente ao dia
    list = [] 
    for i in range(len(arr)):
        if arr[i] == 0:
            list.append(i) #a lista foi criada para pegar os dias que tiveram faturamento 0
    arr = np.delete(arr, list) #funcao para remover os elementos de acordo com os dias do vetor list
    media = np.mean(arr)
    minimo = np.min(arr)
    maximo = np.max(arr)
    dias = []
    for i in range(len(arr)):
        if arquivo[i]["valor"] > media:
            dias.append(i+1) #vetor gerado para anexar os dias que teve faturamento maior que a media
    
    print(f'\nO valor mínimo do mês é: R$ {minimo:.2f}')
    print(f'O valor máximo do mês é: R$ {maximo:.2f}')
    print(f'A média do mês é: R$ {media:.2f}')
    print(f'Os dias que ficaram acima da média foram: {dias}\n')

with open("C:\dados_do_mes\dados.json") as file: 
    data = json.load(file) #leitura do arquivo json

calcMes(data)

