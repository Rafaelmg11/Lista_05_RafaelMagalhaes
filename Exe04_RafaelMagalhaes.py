#Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Dipois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!"
#e adicione 1 à contagem
#Em seguida, pergunte se ela quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira convidar mais ninguem para festa e ,em seguida monstre quantas pessoas foram convidadas para a festa

nome = (input("Insira o nome do convidado: "))
print("{} foi adicionado(a) com suceso no convite!".format(nome))

resposta = (input("Você deseja convidar mais alguém para a festa? "))
resposta.lower()

i = 1

if resposta == 'sim' or resposta == 's':
    while resposta == 'sim' or resposta == 's':
        nome = (input("Insira o nome do convidado: "))
        print("{} foi adicionado(a) com suceso no convite!".format(nome))

        resposta = (input("Você deseja convidar mais alguém para a festa? "))

        i+=1

    print("Foram convidadas {} pessoas.".format(i))

else:
    print("Foram convidadas {} pessoas".format(i))


print("Rafael de Almeida de Magalhães")
print("FIM DO PROGRAMA!")
