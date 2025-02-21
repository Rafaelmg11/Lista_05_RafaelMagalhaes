#Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".

num = int (input('Digite um número entre 15 e 20: '))

while num <= 15 or num >= 20:
    if num <= 15:
        print("Muito Baixo! Tente Novamente!")
        num = int (input('Digite um número entre 15 e 20: '))

    elif num >=20:
        print("Muito Alto! Tente Novamente")
        num = int (input('Digite um número entre 15 e 20: '))

print("Obrigado!")

print("Rafael de Almeida de Magalhães")
print("FIM DO PROGRAMA!")
