
Nome = input("Qual é o seu nome completo: ")
while True:
    if Nome.strip == "":
         print("Voce deixou vazio")
    else:
         break
    Nome = input("Qual é o seu nome")





Idade = int(input("Qual é a sua idade: "))

Informacoes = input("Voce quer que eu te mostre suas informaçoes? (Responda sim ou nao) ")
if Informacoes == "nao":
        print("Ok, obrigado por atualizar seu cadastro")

elif Informacoes == "sim":
    

    print("Certinho, obrgiado por atualizar seus dados", "\n","\n")

    print("O seu nome é", Nome, "\n")

    print("Voce tem", Idade, "Anos", "\n")
