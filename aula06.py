#exercicio2

litros = int(input('Quantos litros:')) # quantidade suco
agua = litros * 0.80 # quantidade de agua
suco = litros * 0.20 # quantidade de suco

print('para fazer {} litros preciso de {} ml de agua e {} ml de suco'.format(litros,agua, suco))

#exercicio4

salario = float(input('Digite o salario do funcionario: '))
vendas = float(input('vendas realizadas:'))
ajuste = vendas * 0.4
final = salario + vendas + ajuste

print('salario total com comisão sera de R${}.'.format(final))

#exercicio5

peso = float(input('insira seu peso:'))

p1 = (peso * 0.15) + peso 
p2 = (peso * -0.20) + peso

print('seu peso é de {}kg, se engordar 15% sera de {} kg, e se emagrecer 20% do peso digitado tera {}kg.'.format(peso,p1,p2))

#exercicio6

salariom = float(input('insira o salario mininmo '))
salriof = float(input('insira salario '))

total = salriof / salariom

print(total)

#exercicio7

tabu = int(input('insira o nuemro da tabuada '))

print('{} X 0 = {}'.format(tabu, tabu*0))
print('{} X 1 = {}'.format(tabu, tabu*1))
print('{} X 2 = {}'.format(tabu, tabu*2))
print('{} X 3 = {}'.format(tabu, tabu*3))
print('{} X 4 = {}'.format(tabu, tabu*4))
print('{} X 5 = {}'.format(tabu, tabu*5))
print('{} X 6 = {}'.format(tabu, tabu*6))
print('{} X 7 = {}'.format(tabu, tabu*7))
print('{} X 8 = {}'.format(tabu, tabu*8))
print('{} X 9 = {}'.format(tabu, tabu*9))
print('{} X 10 = {}'.format(tabu, tabu*10))

#exercicio8

anoatual = int(input('insira o ano atual:'))
anonascimento = int(input('insira o ano de nasciemnto:'))

anos = anoatual - anonascimento
meses = anos * 12
dias = meses * 30
semanas = dias // 7

print('voce tem {} anos com {} meses {} dias e {} semanas'.format(anos, meses, dias, semanas))

#exercicio9

salario = 1200
c1 = 200
c2 = 120

c3 = c1 * 0.02
c4 = c2 * 0.02

c5 = c1 + c2 + c3 + c4
totaldes = salario - c5

print('salario total sera de {}'.format(totaldes))

#--------------------------------------------
#exemoplo da aula de string

nome = 'Rafael Gonçalves da Silva'

#imprimir todos os pares
print(nome[::2])

#imprimir todos os impares
print(nome[1::2])

#primeiro nome
print(nome[:6])

#ultimo nome
print(nome[20:])