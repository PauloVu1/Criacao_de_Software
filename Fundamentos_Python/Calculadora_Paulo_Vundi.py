# Calculadora

num1 = int(input( "digite o primeiro numero: "))
operacao = input("Digite a operação (+.-,*,/):")
num2 = int(input( "digite o primeiro numero: "))
 
if operacao == "+":
        print("o resultado da soma é =", num1+num2) 
elif operacao == "*":
        print ("o resultado da multiplicação é =", num1*num2) 
elif operacao == "-":
    print ("o resultado da subtração é =", num1-num2) 
elif operacao == "/":
   print ("o resultado da divisão é =", num1/num2)
else:
    print ("Operação inválida 😭, tente novamente... Tu consegues💪!")      
     
   