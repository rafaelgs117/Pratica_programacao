#inicio a IF, ELIF e ELSE
aluno = str(input('insira nome do aluno '))
n1 = float(input('insira a nota1 '))
n2 = float(input('insira a nota2 '))
m = (n1 + n2)/2

if 6 >= m <= 10:
 situacao = 'aprovado'

elif 4 <= m < 6:
 situacao = 'recuperacao'

elif 0 >= m < 4:
 situacao = 'reprovado'

else:
 situacao = 'dados invalido'
 print('verifique informação')

print('o aluno {} fechou semestre com media {}.\nSituação: {}'.format(aluno,m,situacao))

#ex2

print('calculo IMC')

peso = float(input('insira o seu peso: '))
altura = float(input('insira sua altura: '))

imc = peso / (altura**2) 

if 18.5 >= imc >= 0:
 print('abaixo do peso')

elif 18.5 <= imc <= 24.9:
 print('peso normal')

elif 25 >= imc <= 29.9:
 print('acima do peso')

elif 30 >= imc <= 34.9:
 print('obesidade 1')

elif 35 >= imc <= 39.9:
 print('obesidade 2')

elif 40 >= imc:
 print('obesidade 3')

print('FIM')

#ex3

maior = None
menor = None
meio = None


a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceuri valor: '))
n = int(input('Informe 1 - Crescente 2 -Decrescente 3 = Maior no meio\n'))

if a > b and a > c:
 maior = a

elif a < b and a < c:
  menor = a
 
elif (a > b and a < c) or (a < b and a > c):
 meio = a

if b > a and b > c:
 maior = b

elif b < a and b < c:
 menor = b
 
elif (b > a and b < c) or (b < a and b > c):
 meio = b

if (c > a and c > b):
 maior = c
 
elif (c < a and c < b):
 menor = c

elif (c > a and c < b) or (c < a and c > b):
 meio = c

if n == 1:
 print('Ordem crescente\n')
 print(menor, meio, maior)

elif n == 2:
 print('Ordem decrescente\n')
 print(maior, meio, menor)
 
elif n == 3:
 print('Maior no meio\n')
 print(menor, maior, meio)
 
print('Nanami!')
