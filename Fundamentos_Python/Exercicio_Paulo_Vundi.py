#Caracteres_especiais


menu = input("Selecione uma funcionalidade: \n\tA) Para maiúscula \n\tB) Para minúscula\n")
mensagem = input("Por favor, escreva a sua mensagem: ")

if menu.upper() == "A":
    print(f"A mensagem em maiúsculas é: \"{mensagem.upper()}\"")
elif menu.lower() == "b":
    print(f"A mensagem em minúsculas é: \"{mensagem.lower()}\"")

