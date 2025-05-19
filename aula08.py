#correção aula dia 07/04

#ex 5

nomeProf = input('informe seu nome: ')
nivel = int(input('informe: \n 1 - Nivel 1\n 2 - Nivel 2\n 3 - Nivel 3: '))
horasTrabalhadas = int(input('Informe quantas horas foram trabalhadas: '))

if nivel == 1:
 salarioProf = horasTrabalhadas * 12.00
elif nivel == 2:
 salarioProf = horasTrabalhadas * 17.00
elif nivel == 3:
 salarioProf = horasTrabalhadas * 25.00
else:
  print('Nivel nao existe')
  salarioProf = 0.0
 
print('O salario do professor {} é de {}.'.format(nomeProf, salarioProf))