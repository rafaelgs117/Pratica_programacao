#Solicite que o usuário insira seu nome completo e apresente apenas o 
#primeiro nome. 
#a. Na vertical 
#b. Na horizontal 

nome = str(input('Digite seu nome completo: ')) #lê o nome
primeiroNome = nome.split()[0] #primeiroNome recebe o primeiro nome

#imprime vertical
print('Seu primeiro nome na verical é: ')
for letra in primeiroNome: #para cada letra em primeiroNome
    print(letra) #imprime a letra

#imprime horizontal
print('Seu primeiro nome na horizontal é: ', end='') #imprime o primeiro nome
for letra in range(len(primeiroNome)): #para cada letra em primeiroNome
    print(primeiroNome[letra], end=' ') #imprime a letra