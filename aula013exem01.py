#usando o while 

cont = 1
soma = 0

while cont <= 10:
    if cont % 2 == 0: # se o número for par
        soma += cont # soma = soma + cont

    print('Dentro do while cont =', cont) #mostra o valor de cont
    print('Dentro do while soma =', soma) #mostra o valor de soma
    cont += 1 # incrementa o cont

print('Fora do while cont =', cont) #mostra o valor de cont
print('Fora do while soma =', soma) #mostra o valor de soma