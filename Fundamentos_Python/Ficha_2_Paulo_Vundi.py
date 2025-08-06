#Ficha_Prática 2
#Formando: Paulo_Vundi
#UFCD: Fundamentos_Python

#Exercicio 1

caracter=str(input("Insira um caracter a sua escolha "))
if caracter.upper():
    print("O caracter escolhido foi maúsculo")
elif caracter.lower():
    print("O caracter escolhido foi minúsculo")

"""   
#Exercíco 2

alfabeto=str(input("introduza um caracter a sua escolha: "))
letras_validas=("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,w,z,ç")
if alfabeto in letras_validas:
    print(f"Letra escolhida permanece maiuscula {alfabeto.upper()}")
else:
   print("O caracter não identificado, tente novamente!")
"""
   
"""
#Exercício 3

x = float(input("Insira a coordenada x: "))
y = float(input("Insira a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no 1º quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no 2º quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no 3º quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no 4º quadrante.")
else:
    print("valor inválido")
"""
"""
# Exercício 4

hora24 = int(input("Insira a hora atual (0 a 23): "))

if 0 <= hora24 < 24:
    if hora24 == 0:
        hora12 = 12
        periodo = "AM"
    elif 1 <= hora24 < 12:
        hora12 = hora24
        periodo = "AM"
    elif hora24 == 12:
        hora12 = 12
        periodo = "PM"
    else:
        hora12 = hora24 - 12
        periodo = "PM"

    print(f"A hora no formato AM/PM é: {hora12} {periodo}")







#Exercício 6

tipo_veículo = input ("Insira o tipo de véiculo (1,2,3 ou 4): ")
idade = int(input("Insira a idade do veículo: " ))


"""



# Exercicio ----

currDate = input("Data[dd/mm/aaaa] = ")
lista_data = currDate.split("/")
daystr = lista_data[0]
monthstr= lista_data [1]
yearstr = lista_data [2]
#daystr, monthstr, yearstr = currDate.split("/")
print(f"{currDate}")