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

cen01 = int(input('quantas moedas de 1 centavo:')) 
cen05 = int(input('quantas moedas de 5 centavo:')) 
cen10 = int(input('quantas moedas de 10 centavo:')) 
cen25 = int(input('quantas moedas de 25 centavo:')) 
cen50 = int(input('quantas moedas de 50 centavo:')) 
real1 = int(input('quantas moedas de 1 real:')) 

total = cen01 + cen05 + cen10 + cen25 + cen50 + real1

conv01 = cen01 * 0.01
conv05 = cen05 * 0.05
conv10 = cen10 * 0.10
conv25 = cen25 * 0.25
conv50 = cen50 * 0.50

dindin = conv01 + conv05 + conv10 + conv25 + conv50 + real1

print('total de moedas guardadas é de',total,' totalizando uma soma de R$',dindin)



