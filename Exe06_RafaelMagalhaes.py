#Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".

num = int (input("Insira um némero entre 15 e 20: "))

if num <= 15:
    print("Muito Baixo!")

elif num >=20:
    print("Muito alto!")

while num != (num > 15 and num <20):
    print("Tente Novamente!")
    num = int (input("Insira um número entre 15 e 20: "))
    if num <= 15:
        print("Muito Baixo!")
        print("Tente Novamente!")
        num = int (input("Insira um número entre 15 e 20: "))
    elif num >= 20:
        print("Muito Alto!")   
        print("Tente Novamente!")
        num = int (input("Insira um número entre 15 e 20: "))  
    else:
        print("Obrigado!")
    break
