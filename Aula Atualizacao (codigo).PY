# Verificação de Voto - Exemplo Simples

# F-STRING (f""): Insere variáveis no texto usando {}
# Exemplo: print(f"Olá {nome}") em vez de print("Olá " + nome)

# Entrada do nome e idade pelo usuário
nome = input("Qual é o seu nome: ")

# Verificar se o nome está vazio e contém apenas letras
while True:
    if nome.strip() == "":
        print("Esse espaço nao pode ficar em branco")
    elif not nome.replace(" ", "").isalpha():
        print("Deve conter apenas letras")
    else:
        break
    nome = input("Digite seu nome: ")

# Entrada da idade
while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Digite apenas números para a idade!")

# Verificação simples
if idade >= 16:
    resultado = f"{nome}, você PODE VOTAR"
else:
    resultado = f"{nome}, você NÃO PODE VOTAR"

print(resultado)

# Perguntar se quer imprimir os dados
imprimir = input("Deseja imprimir os dados? (s/n): ")

if imprimir.lower() in ['s', 'sim']:
    print(f"\nNome: {nome}")
    print(f"Idade: {idade}")
    print(f"Status: {resultado}")