#fazer o usuario escolher onde comça a contagem e onde termina
soma = 0
par = 0
impar = 0
mult3 = 0

val1 = int(input("Digite o valor inicial: "))
val2 = int(input("Digite o valor final: "))

for n in range(val1, val2+1): # o +1 é para incluir o valor final na contagem
    soma = soma + n
    if n % 2 == 0: # se o resto da divisao de n por 2 for igual a 0 n = par
     par = par + n 
    else:
       impar = impar + n # se o resto da divisao de n por 2 for diferente de 0 = impar
    if n % 3 == 0:
       mult3 = mult3 + n

print(soma)
print(par)
print(impar)
print(mult3)
