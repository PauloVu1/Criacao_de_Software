# Exercicio 1 - calcular a área do rectângulo

"""
import math

largura = int(input("digite a largura do rectângulo em cm "))
comprimento = int(input("digite o comprimento do em cm "))
area=comprimento*largura
print("A área do rectângulo é igual a:", area, "cm2" )
"""
# Exercício 2: Desenvolver um programa que leia o valor do raio de uma circunferência e imprima a sua area e o seu perimetro.
'''
import math

raio = float(input("Qual é o raio da circunferência "))
pi = 3.1415
area_circ = math.pi*raio**2
perimetro_circ = 2*math.pi*raio
print(f"area = {area_circ}")
print(f"perimetro = {perimetro_circ}")

'''

#Exercicio 3: teorema de de Pítagoras

'''
#from math import sqrt 
import math #- importa toda a biblioteca
a = 38
b = 45
h1 = math.sqrt(pow(a, 2) + pow(b, 2))
h2 = math.sqrt(a*a + b*b)
h3 = math.sqrt(a**2 + b**2)
print(f" {h1} " )
print(f" {h2} " )
print(f" {h3} " )

'''
# Exercicio 4 - Converter graus Fahrenheit para graus celsius

'''
Fahrenheit = float(input("Qual é a temperatura em (graus celsios):"))
Celsius = (5/9 *(Fahrenheit-32))
print (f"{Fahrenheit} graus Fahrenheit é = a {Celsius} graus Celsius")

'''
# Exercicio 5



#Exercicio 6: 

velocidade= input("introduza a velocidade media percorrida")
duração= input("Introduza o tempo aproximado da duração da viagem")
distancia_percorrida = velocidade*duração

print(f" A distancia percorrida foi de {distancia_percorrida} km/h")




# Exercicio 8

valor = 846
valor = int(input("Insira um valor com tres digitos: "))

# % - resto da divisão
# // -  numero sem a casa decimal

num1 = valor % 10     # 184,5 - 6
valor = valor // 10   # valor - 184

num2 = valor % 10
valor = valor // 10

num3 = valor % 10
valor = valor // 10

soma = num1 + num2 + num3

print("soma ")