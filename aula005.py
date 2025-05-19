saudacao = 'Olá turma de 2025 1'

print('A saudação tem',len(saudacao),'caracteres.')
print(saudacao.lower())

print(saudacao.replace('2','1'))

print(saudacao.startswith("Olá"))

print(saudacao.endswith('3'))

print(saudacao.count('2'))

#exemplo 1 alterar a primeira letra para maisculo, e depois fazer a primeira letra de cada palavra maiscula

frase1 = 'a tecnologia move o mundo.'

print(frase1.capitalize()) #priemira letra

print(frase1.title()) #primeira letra cada palavra

#lista ecercicio

#1
#Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais 
#conseguiu poupar. Faça um algoritmo para ler a quantidade de cada tipo de 
#moeda, e imprimir o valor total economizado, em reais. Considere que 
#existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. 
#Não havendo moeda de um tipo, a quantidade respectiva é zero.  

cen01 = int(input('quantas moedas de 1 centavo:'))  #entrada de informaçoes
cen05 = int(input('quantas moedas de 5 centavo:')) 
cen10 = int(input('quantas moedas de 10 centavo:')) 
cen25 = int(input('quantas moedas de 25 centavo:')) 
cen50 = int(input('quantas moedas de 50 centavo:')) 
real1 = int(input('quantas moedas de 1 real:')) 

total = cen01 + cen05 + cen10 + cen25 + cen50 + real1 #calculo do total de moedas

conv01 = round(cen01 * 0.01, 2) #calculo de cada moeda, round para arredondar 2 casas decimais, valor saira em reais
conv05 = round(cen05 * 0.05, 2)
conv10 = round(cen10 * 0.10, 2)
conv25 = round(cen25 * 0.25, 2)
conv50 = round(cen50 * 0.50, 2)

dindin = conv01 + conv05 + conv10 + conv25 + conv50 + real1 #calculo do valor total em reais

print('total de moedas guardadas é de',total,' totalizando uma soma de R$',dindin)

#2
 
#Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco 
#de maracujá. Faça um algoritmo para calcular quantos litros de água e de 
#suco são necessários para se fazer X litros de refresco (informados pelo 
#usuário). 

agua = 8 #valores em litros
suco = 2

litros = float(input('quantos litros de refresco deseja fazer:'))

agua_total = litros * agua #calculo de agua e suco
suco_total = litros * suco 

print('para fazer',litros,'litros de refresco é necessário',agua_total,'litros de agua e',suco_total,'litros de suco')

#3

#Faça um algoritmo que receba o preço de um produto, calcule e mostre o 
#novo preço, sabendo-se que este sofreu um desconto de 10%. 

produto = float(input('digite o valor do produto:')) #entrada de informaçoes

desconto = round(produto * 0.10, 2) #calculo do desconto round para arredondar

novo = produto - desconto #calculo do novo valor

print('o valor do produto é de R$',produto)
print('o valor do desconto é de R$',desconto)
print('o valor do produto com desconto é de R$',novo)


#4

#Um funcionário recebe um salário fixo mais 4% de comissão sobre as 
#vendas. Faça um algoritmo que receba o salário fixo de um funcionário e o 
#valor de suas vendas, calcule e mostre a comissão e o salário final do 
#funcionário. 

salario = float(input("digite o salario do funcionario:")) #entrada de informaçoes
vendas = float(input("digite o valor das vendas:")) 

comissao = round(vendas * 0.04, 2) #calculo da comissao
salario_final = salario + comissao #soma do salario + comissao

print('O salario do funcionario é de R$',salario,'e a comissão é de R$',comissao,'o salario final é de R$',salario_final)

#5

#Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre: 
#a) o novo peso se a pessoa engordar 15% sobre o peso digitado; 
#b) o novo peso se a pessoa emagrecer 20% sobre o peso digitado. 


#6

#Faça um algoritmo que receba o valor do salário mínimo e o valor do salário 
#de um funcionário, calcule e mostre a quantidade de salários mínimos que 
#ganha esse funcionário.


#7
#Faça um algoritmo que calcule e mostre a tabuada de um número digitado 
#pelo usuário. 

#8

#Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano 
#atual, calcule e mostre: 
#a) a idade dessa pessoa em anos; 
#b) a idade dessa pessoa em meses; 
#c) a idade dessa pessoa em dias; 
#d) a idade dessa pessoa em semanas.  

#9

#João recebeu seu salário de R$1200,00 e precisa pagar duas contas (C1 = 
#R$200,00 e C2 = R$120,00) que estão atrasadas. Como as contas estão 
#atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um 
#algoritmo que calcule e mostre quanto restará do salário do João. 