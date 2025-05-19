#somar numeros pares de 1 a 10
#somar os numeros impar de 1 a 10
#somar numeros multiplos de 3 que estao de 1 a 10

soma = 0
par = 0
impar = 0
mult3 = 0

for n in range(1,11):
    soma = soma + n # soma = soma + n é a mesma coisa que soma += n, ou seja, soma = soma + n
    if n % 2 == 0: # se o resto da divisao de n por 2 for igual a 0 n = par
     par = par + n 
    else:
       impar = impar + n # se o resto da divisao de n por 2 for diferente de 0 = impar
       
    if n % 3 == 0: # se o resto da divisao de n por 3 for igual a 0 ele é multiplo de 3
      mult3 = mult3 + n
        

print(soma)
print(par)
print(impar)
print(mult3)