def inverter(frase): #funcao que irá inverter palavra ou frase
    return frase[::-1] #foi utilizado a notacao de slice, fara a leitura de todos os caracteres com passo negativo

frase = inverter(input("\nDigite uma palavra ou frase para ser invertida: "))
print(f"A palavra ou frase invertida fica assim: {frase}\n")