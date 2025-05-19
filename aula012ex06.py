#Solicite que o usuário insira seu nome completo e informe quantos caracteres 
#ele possui. 

nome = str(input('Digite seu nome completo: ')) #lê o nome
tamanho = len(nome) #tamanho recebe o tamanho do nome

print(f'Seu nome completo é {nome} e possui {tamanho} caracteres.') #imprime o nome e o tamanho
# print('Seu nome completo é {} e possui {} caracteres.'.format(nome, tamanho)) #outra forma de imprimir
