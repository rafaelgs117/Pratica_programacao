#Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta 
#quantos destes valores são negativos.

valores = int(input('Quantos valores você quer digitar? ')) #quantidade de valores
negativos = 0 #inicializa negativos

for n in range(1, valores + 1): #n inicia em 1 e vai ate o valor digitado + 1
    valor = float(input(f'Digite o {n}º valor: ')) #lê o valor 
    #valor = float(input('Digite o {}º valor: '.format(n))) 
    if valor < 0: #se o valor for menor que 0
        negativos += 1 #negativos = negativos + 1

print(f'Você digitou {negativos} valores negativos.')
#print('você digitou {} valores negativos.'.format(negativos))