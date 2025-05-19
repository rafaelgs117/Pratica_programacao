#faça um algoritimo(programa) que leia um falor incial A e imprima a sequencia de valores
# do calculo de A! e o seu resultado. (EX: 5! = 5*4*3*2*1 = 120)

fatorial = int(input('Informe um valor: ')) #inicializa o fatorial
resultado = 1 #inicializa o resultado

for n in range(1, fatorial + 1): #loop para calcular o fatorial
    resultado = resultado * n #multiplica o resultado pelo valor atual do loop

print(f'O fatorial de {fatorial} é {resultado}') #imprime o resultado

#outra forma de fazer
fatorial = int(input('Informe um valor: ')) #inicializa o fatorial
resultado = 1 #inicializa o resultado
for n in range(fatorial, 0, -1): #loop para calcular o fatorial
    resultado = resultado * n #multiplica o resultado pelo valor atual do loop

print(f'{fatorial}! = {resultado}') #imprime o resultado


