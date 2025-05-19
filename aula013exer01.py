#Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 3 
#centímetros por ano. Construir um algoritmo que calcule e imprima quantos anos serão 
#necessários para que Juca seja maior que Chico. USAR O WHILE

chico = 1.50
juca = 1.10
ano = 0

while juca < chico:
    chico = chico + 0.02
    juca = juca + 0.03
    ano = ano +1

print(f'Juca sera maior que Chico em {ano} anos')
