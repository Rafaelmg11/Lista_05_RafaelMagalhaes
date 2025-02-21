#Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.

num = []

numdig = int (input("Digite um número: "))

num.append(numdig)

if numdig != 0:
    while numdig != 0:
        numdig = int (input("Digite um número: "))
    

        if numdig in num:
            print("Valor repetido!")

        else:
             num.append(numdig)

    if numdig == 0:
        num.remove(0)
        print("Lista:",num)

        i = len(num)

        print("A lista tem {} números".format(i))

print("Rafael de Almeida de Magalhães")
print("FIM DO PROGRAMA!")

    
