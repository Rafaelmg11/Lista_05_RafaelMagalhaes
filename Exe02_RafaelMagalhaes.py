#EXE 002 - Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem “
#  O último número que você digitou foi um [número] " e pare o programa.

cont = 0

while cont < 5:
    num = (input("Digite um número: "))
    cont+=+1
print("O ultimo número que você inseriu foi: {}".format(num))

