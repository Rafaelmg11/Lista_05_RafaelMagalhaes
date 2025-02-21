#Crie uma variavel chamada "adivinha" e defina o valor como 50.
#Peça ao usuario para inserir um número. Embora o palpite não seja o mesmo que o valor do "adivinha", diga a ele se o palpite é  muito alto ou muito baixo e peça que ele dê outro
#palpite. Se ele inserir o mesmo valor que "adivinha",exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!"

adivinha = 50
i = 1

palpite = int (input("Insira o seu palpite: "))

if palpite != adivinha:
    while palpite != adivinha:
        if palpite > adivinha:
            print("Palpite muito alto!")
        elif palpite < adivinha:
            print("Palpite muito baixo!") 

        palpite = int (input("Insira o seu palpite: "))

        

        i+=1

    print("Parabéns! Você acertou o número em {} tentativas!".format(i))

elif palpite == adivinha:
    print("Parabéns você acertou de primeira! ")

print("Rafael de Almeida de Magalhães")
print("FIM DO PROGRAMA!")
