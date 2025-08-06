""" 
quantidade = int(input("Quantas vezes deseja repetir a sms? R:"))
for i in range (1, quantidade +1):
    print(f"{i}  o numero de vezes foi")
     
"""
 
While True:
    quantidade = int(input("Quantas vezes deseja repetir a sms? R:"))
    i = 1
    while i <= quantidade:
        print (f"{i}: Esta é a mensagem.")
        i += 1
    if i<quantidade:
        break

