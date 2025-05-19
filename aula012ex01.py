#exe01
#fazer algoritimo para ler altura de X pessoas, esse programa devera calcular e mostrar:
#a menor altura do grupo;
#a maior altura do grupo;

menorAltura = 0 #inicializa menorAltura
maiorAltura = 0 #inicializa maiorAltura
somaAltura = 0 #inicializa somaAltura

quantidadePessoas = int(input("Quantas pessoas você quer cadastrar? "))

for n in range(quantidadePessoas):#joga o valor dentro de quanPessoa dentro de n de for
    altura = float(input('Digite a altura da pessoa da posição {}: '.format(n + 1)))#indica altura e posição
    somaAltura += altura #somaAltura recebe altura, somaAltura = somaAltura + altura
    
    if n == 0: #se n for igual a 0
        menorAltura = altura #menorAltura recebe altura
        maiorAltura = altura #maiorAltura recebe altura
    
    else:
        if altura < menorAltura: #se altura for menor que menorAltura
            menorAltura = altura #menorAltura recebe altura
        if altura > maiorAltura: #se altura for maior que maiorAltura
            maiorAltura = altura #maiorAltura recebe altura

print('A menor altura do grupo é de {} metros'.format(menorAltura))
#print(f'A menor altura do grupo é de {menorAltura} metros')
print('A maior altura do grupo é de {} metros'.format(maiorAltura))
#print(f'A maior altura do grupo é de {maiorAltura} metros')