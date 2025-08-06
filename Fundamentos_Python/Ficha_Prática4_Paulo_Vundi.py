"""
#Ficha_Prática_4
#Formando: Paulo_Vundi
#UFCD: Fundamentos_Python
"""    


#Exercício_1:  feito

palavra=str(input("Digite uma palavra: "))
print(palavra[0])
print(palavra[-1])


#Exercício_2: feito
frase=str(input("Escreva uma palavra: "))
print(f"Os caracteres do 2º e 4º indice são: {frase[1:5]})

#Exercício_3: feito

frase=str(input("Digite uma frase: "))
print(len(frase))

# Exercício_4: feito

frase=str(input("Escreva uma frase: "))
print(f" Os caracteres pares são: {frase[::2]}")

#Exercício_5: feito

frase1 = str(input("Introduza uma frase ou palavra: "))
frase2 = str(input("Introduza uma nova frase ou palavra: "))
união = "_".join([frase1, frase2])
print(união)

#Exercício_6: feito

frase=str(input("Digite uma frase: "))
print(frase*5)

#Exercício_7: feito

frase = str(input("Digite uma frase e um caracter: "))
caracter = str(input("Digite um caracter: "))
quantidade = frase.count(caracter)
print(f"o caracter {(caracter)} aparece {quantidade} vezes na frase: ")

#Exercício_8: feito!

frase = str(input("Digite uma frase: "))
palavra = str(input("Digite uma palavra: "))
quantidade = frase.count(palavra)
print(f"a palavra {(palavra)} aparece {quantidade} vezes na frase: ")

#Exercício_9:feito

frase=str(input("Digite uma frase: ")).upper()
print(frase)

#Exercício_10:feito
frase=str(input("Digite uma frase: ")).lower()
print(frase)

#Exercício_11:feito
frase=str(input("Digite uma frase com espaços no inicio e no fim: ")).strip()
print(frase)

