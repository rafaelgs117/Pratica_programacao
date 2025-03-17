
#exercicio 1
#Criar 2 valores e compara se eles são iguais ou não:

valor1 = int(input('Insira o primeiro valor: ')) #valor inteiro
valor2 = int(input('Insira o segundo valor: '))

resultado = valor1 == valor2 #ira comparar os valores 1 e 2

print('O valor 1 é ',resultado,' comparado ao valor 2') #mostrara a comparação com uma frase mostada

#exercicio2
#ltere o codigo para dar True
print(('a' == 'a' or 'b' == 'a') and ((1 > 1) and 2 <= 2))

#RESPOSTA
print(('a' == 'a' or 'b' == 'a') and ((1 >= 1) and 2 <= 2))

#exercicio3
#A
n = 10 % 2 #valor de n é 0

c1 = 9> n = true 
c2 = 0 > n = fause
r1 = not c1 and c2 = false
r2 = c1 or not c2 = true

print(c1, c2)
print(r1, r2)

#B
n = 5-10 #valor de n é -5

c1 = -10>n = false
c2 = -15>n = false
r1 = c1 or c2 = false
r2 = c1 and c2 = false

print(c1,c2) #imprime os valores de c1 e c2 conforme a ordem acima
print(r1,r2)

#exercicio5

celcios = float(input('Insira a temperatura em celcios: ')) 
fahrenheit = celcios * 1.8 + 32  #calculo da conversão de celcios para fahrenheit

print('A temperatura ',celcios,'graus celcios convertida paara fahrenheit é ',fahrenheit,'graus')

#exercicio 6

hora_normal = 10 #valores referentes a cada hora trabalhada
hora_extra = 15 #valores referentes a cada hora extra

horas_trabalhadas = float(input('Quantas horas foram trabalhadas pela funcionaria Alice: '))
horas_estras = float(input('Insira as horas extras da funcionaria Alice: '))

salario = ((horas_trabalhadas * hora_normal) + (horas_estras * hora_extra)) #calculo do salario
desconto = salario % 0.10 #calculo do desconto
total = salario - desconto #calculo do salario com desconto

print('o salario trabalhado por horas normais e extras é de R$',salario,' menos 10% de desconto R$',total)

#exercicio 7

lata = 350.0 #valor referente a ml 
garrafa = 600.0 #valor referente a ml 
litro = 2.0 #valor referente a litro

compra1 = int(input("Latas compradas: "))
compra2 = int(input("Garrafas compradas: "))
compra3 = int(input("Garafas de 2L compradas: "))

con_lata = lata * 0.001 * compra1 #conversão de ml para litros
con_garrafa = garrafa * 0.001 * compra2 #conversão de ml para litros
con_litro = litro * compra3 #conversão de litros para litros

total = con_lata + con_garrafa + con_litro #soma total de litros comprados

print('Total de litros comprado é de ',total)
print(con_lata, con_garrafa, con_litro)


#EXERCICIO 8
#Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de
#um bar.
#Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um
#deve pagar, mas faça com que Carlos e André não paguem centavos. Ex:
#uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para
#André e R$35,53 para Felipe.

carlos = float(input('Digite o valor da conta de Carlos: '))# valor Carlos
andre = float(input('Digite o valor da conta de Andre: '))# valor Andre
felipe = float(input('Digite o valor da conta de Felipe: '))# o valor de Felipe 

total = carlos + andre + felipe # soma total das contas
total_carlos = total //3 #divisão exata de Carlos e Andre
total_andre = total //3
total_felipe = total - (total_andre + total_carlos) # Felipe sera a conta dele menos a a soma de Carlos e Aandre

print('Carlos e André pagaram cada um R$',total_andre,' e Felipe R$',total_felipe) # imprime o valor, como Carlos e Aandre sera o memso valor basta chamar total de um dos 2
