def fibonacci(num):
    seq = [0,1] #a sequencia começa com esses valores
    if num==1:
        print('[0]') #caso digitar 1 irá retornar o primeiro valor da sequencia
    elif num==2:
        print(seq) #caso digitar 2 irá retornar a sequencia inicial
    else:
        while(len(seq)<num):
            seq.append(0) #complementa o vetor seq com zeros de acordo com o tamanho de numeros informado
        if num == 0:
            print("Digite um valor acima de 0")
        else:
            seq[0]=0
            seq[1]=1
            for i in range(2,num):
                seq[i]=seq[i-1]+seq[i-2]
            print(f'\nSequência de Fibonacci gerada com {num} valores: {seq}')
            if num in seq:
                print(f'\nO numero {num} está na sequência de Fibonacci.')
            else:
                print(f'O numero {num} não está na sequência de Fibonacci.\n')
            
fibonacci(int(input('Informe um número para gerar a sequência de Fibonacci: ')))