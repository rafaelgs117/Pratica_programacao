#exemplo01 
'''
from time import sleep 
 
cR = 10

for i in range(1,11): # começa em 1 e vai ate 10, apos o 11 é como se tivese um ,1 vai uma casa por vez
    print(cR)
    cR -= 1 # é a mesma coisa que cR = cR -1
    sleep(1) # espera 1 segundo em outras linguagens é 1000 milissegundos
    
print("Feliz ano novo!")

#outra forma 

for n in range(10, 0, -1): # começando em 10, ira ate 1, decrementando uma casa de cada vez
    print('n = ',n)
    sleep(1)

print("feliz ano novo!")
'''
#exemplo02

#soma = 0

#for n in range(1, 5): #começa em 1 e soma um por vez ate n se igual a 10
#    soma = soma + n
#    print(soma)

#ex01 
#somar numeros pares de 1 a 10
#somar os numeros impar de 1 a 10
#somar numeros multiplos de 3 que estao de 1 a 10
'''
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
'''
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




