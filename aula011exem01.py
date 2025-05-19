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