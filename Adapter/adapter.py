def adap(nome_arquivo):
    agenda = [] 
    agenda2 = []## Armazenara os números finais
    arquivo = open(nome_arquivo,"r") 

    ## Navegando pelo arquivo e salvando as listas em um array
    for linha in arquivo: 
        numeros = arquivo.readlines()

    ## Navegando pelo array e retirando os caracteres não essenciais
    tamanho = len(numeros)
    for i in numeros: 
        for n in i:
            if n == '(' or n == ')' or n == ' ' or n == '-' or n == '\n':
                continue
            else:
                agenda.append(n)
        agenda = ''.join(agenda)
        agenda2.append(agenda)
        agenda=[]

    return agenda2
    arquivo.close()

nome_arquivo = "numero.txt"
agenda2 = adap(nome_arquivo)
for i in agenda2:
    print(i)
