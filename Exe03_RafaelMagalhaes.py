#Peça ao usuario para inserir um numero e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar "s",diga para inserir outro número e continuar adicionando números e somando até que ele não responde 's'.
#Depois que o loop for interrompido,exiba total

num1 = int (input("Digite um número: "))
num2 = int (input("Digite um número: "))

soma = num1 + num2

resposta = input("Deseja adicionar outro número? ")
resposta.lower()

if resposta == 's':
    while resposta == 's':
        num3 = int (input("Digite um número: "))
        soma = soma + num3
        resposta = input("Deseja adicionar outro número? ")
        
    print("Total:",soma)

else:
    print("Total:",soma)


