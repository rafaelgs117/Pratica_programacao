#Uma rainha requisitou os serviços de um monge, o qual exigiu o pagamento em grãos de trigo da seguinte maneira: 
#os grãos de trigo seriam dispostos em um tabuleiro de xadrez, de tal forma que a primeira casa do tabuleiro 
#tivesse um grão, e as casas seguintes o dobro da anterior. Construa um algoritmo que calcule quantos grãos de 
#trigo a Rainha deverá pagar ao monge. Um tabuleiro tem 64 casas.

total = 0
graos = 1

for n in range(1, 65): #loop 
    total += graos # soma
    graos *= 2 # multiplica por 2   
    print('Casa {}: {} grãos'.format(n, graos)) # imprime a quantidade de grãos
print('Total de grãos: {}'.format(total)) # imprime o total

#