# Em uma eleição presidencial existem quatro candidatos. Os votos são 
#informados através de códigos. Os dados utilizados para a contagem dos 
#votos obedecem à seguinte codificação:   
#a. 1,2,3,4 = voto para os respectivos candidatos; 
#b. 5 = voto nulo; 
#c. 6 = voto em branco; 
#d. Elabore um algoritmo que leia o código do candidato em um voto. 
#Calcule e escreva: 
#e. total de votos para cada candidato; 
#f. total de votos nulos; 
#g. total de votos em branco; 
#Faça um algoritmo para ler pelo menos 100 votos. 

cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0

for n in range(1, 6):
    voto = int(input(f'Insira o seu voto :'))

    if voto == 1:
        cand1 = cand1 + 1
    elif voto == 2:
        cand2 = cand2 + 1
    elif voto == 3:
        cand3 = cand3 + 1
    elif voto == 4:
        cand4 = cand4 + 1
    elif voto == 5:
        nulo = nulo + 1
    elif voto == 6:
        branco = branco + 1
    else:
        print('Opção invalida.')

print(f'Votos para o candidato 1: {cand1}')
print(f'Votos para o candidato 2: {cand2}')
print(f'Votos para o candidato 3: {cand3}')
print(f'Votos para o candidato 4: {cand4}')
print(f'Votos nulos: {nulo}')
print(f'Votos em branco: {branco}')
