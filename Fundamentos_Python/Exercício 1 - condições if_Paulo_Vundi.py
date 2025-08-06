#and, or e not

# Escrever um programa que converta a nota de aluno para a uma classificação

nota = float(input("introduza a nota do aluno (valor entre 0 e 20) "))

if nota < 0 or nota > 20:
    print ("Valor inválido... ")
else:

    if nota == 0 or nota <= 9:
        print("chumbado")
    elif nota == 10 or nota <= 13:
        print("Suficiente")
    elif nota == 14 and nota <= 15:
        print("Bom")  
    elif nota == 16 and nota <= 17:
        print("Muito bom")
    elif nota == 18 or nota <=20:
        print("Excelente")
    #else:
      # print("Valor incorreto!")
           
 
