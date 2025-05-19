#tabuada usando WHILE

tabuada = int(input('Digite a tabuada que vocw dejesa: ')) #usuario indica a tabuada que ele quer.
inicio = 1 #vai inicia em 1
fim = 10 #vai terminar em 10
cont = inicio #cont vai ser igual a inicio

while cont <= fim: #enquanto cont for menor ou igual a fim 
    print(f'{tabuada} X {cont} = {tabuada*cont}') #imprime a tabuada
    cont += 1 #cont vai ser igual a cont + 1

