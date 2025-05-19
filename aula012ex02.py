#fazer um algoritimo(programa) que gere e escreva os numeros impares entre 100 e 200. 

impares = 0 #contador de impares
inicio = 100 #iniciação do intervalo
fim = 200 #final do intervalo

for n in range(inicio, fim + 1): #loop para percorrer o intervalo
    if n % 2 != 0: #verifica se o numero é impar
        impares += 1 #incrementa o contador de impares
        print(n) #imprime o numero impar dentro do intervalo pedido