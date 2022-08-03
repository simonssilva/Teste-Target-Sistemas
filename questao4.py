import numpy as np

def porcentagem(valor, total): #funcao para calcular porcentagem
    return round(((100 * valor)/total), 2)

#Valores recolhidos para calculo definidos em um dicionario
valores = { "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "Outros" : 19849.53}

total = sum(valores.values()) #soma dos valores do dicionario
print(f'\nValor total do faturamento das distribuidoras: R$ {total}')
for i in valores:
    print(f'Porcentagem do faturamento de {i} com base no total é {porcentagem(valores[i], total)} %')

print()