def ex1():
    numero = int(input("Insira um número: "))
    for i in range(0, 26):
        print(numero*i)
    
def ex2():
    print("Versão1: Quantidade de funcionarios delimitada pelo utilizador")
    print("="*63)

    numero_empregados = int(input("Quantos funcionários deseja considerar? : "))
    salarios = []

    for i in range(numero_empregados):
        salario = float(input(f"Introduza o salario do empregado: "))
        salarios.append(salario)
    if len(salarios) > 0:
        media = sum(salarios) / len(salarios)
        print(f"A média salaria é de: {media:.2f} {i+1} €")
    else:
        print("Sem salário introduzido!")

    print("Versão2: A introdução termina se o valor for nulo ou negativo")
    print("="*63)  

    salario = []
    print("Introduza os salarios (Digite 0 ou valor negativo para terminar): ")

    while True: 
        salario = float(input("introduz o salario: "))
        if salario <= 0:
            print("Operação terminada!")
            break
        salarios.append(salario)
    if len(salarios) > 0:
        media = sum(salarios) / len(salarios)
        print(f"A média salaria é de: {media:.2f} €")
    else:
        print("Salário inválido")

def ex3():
    produto_alimentar = []
    produto_nao_alimentar = []

    while True:
        tipo_produto = input("Introduza o tipo de produto (alimentar ou nao-alimentar): ").strip().lower()
        try:
            preco = float(input("Introduza o preço do produto em €: "))
        except ValueError:
            print("Preço inválido. Tente novamente.")
            continue

        if preco <= 0:
            print("Introdução finalizada!")
            break

        if tipo_produto == "alimentar":
            produto_alimentar.append(preco)
        elif tipo_produto == "nao-alimentar":
            produto_nao_alimentar.append(preco)
        else:
            print("Produto não consta da base de dados... Por favor, tente novamente!")

    qtd_alimentar = len(produto_alimentar)
    qtd_nao_alimentar = len(produto_nao_alimentar)
    qtd_total = qtd_alimentar + qtd_nao_alimentar

    soma_alimentar = sum(produto_alimentar)
    soma_nao_alimentar = sum(produto_nao_alimentar)
    preco_total_sem_iva = soma_alimentar + soma_nao_alimentar

    iva_alimentar = soma_alimentar * 0.06  
    iva_nao_alimentar = soma_nao_alimentar * 0.23 

    preco_total_com_iva = preco_total_sem_iva + iva_alimentar + iva_nao_alimentar

    print("\n--- Talão de Compras ---")
    print("Produtos alimentares:", qtd_alimentar)
    print("Produtos não alimentares:", qtd_nao_alimentar)
    print("Total de produtos:", qtd_total)
    print("Preço total sem IVA: €{:.2f}".format(preco_total_sem_iva))
    print("Preço total com IVA: €{:.2f}".format(preco_total_com_iva))

def ex4():
    while True:
        m = int(input("Insira o valor de m = : "))
        n = int(input("Insira o valor de n = : "))
        
        if m >= 100 and m < n and n <= 999:
            break
        else:
            print("Valores inválidos!")
        
    for numero in range(m, n +1):
            a= numero// 100
            b= (numero//10) % 10
            c= numero % 10
                    
            soma = a**3 + b**3 + c**3
                        
            if numero == soma:
                print(f"O numero {numero} é igual a soma do cubo dos seus algarismos ({soma}")
            else:
                print("Não corresponde ao pedido, tenta novamente!")
        
def ex5():
    
    print("***** Multiplos de 3 que não são de 5*****")
    print("*"*65)
    
    valor1 = int(input("Insira um valor inicial: "))
    valor2 = int(input("Insira valor final: "))
    
    if valor1 <= 0:
        print("valor inválido! tente um numero positivo")
    elif valor2 <= 0:
        print("valor inválido! tente um numero positivo")
    elif valor1 > valor2:
        print("valor inválido! o valor inicial tem que ser maior do que o valor final")
    else:
        print(f"os valores introduzidos entre {valor1} e {valor2}:")
              
    contador = 0
    
    for numero in range(valor1, valor2 +1):
        if numero % 3 == 0 and numero % 5 != 0:
            print (numero)
            contador += 1
    print("*"*65)
    print(f"Foram encontrados os seguintes multiplos:{contador}")
    
    if contador == 0:
        print("Nennhum valor foi encontrado! Tente novamente mais tarde.")

def ex6():
    
    print("__Introduza um número inteiro positivo__")
    numero = int(input("Introduza um numero: "))
    
    if numero <= 0:
        print("Introduziste um valor negativo ou nulo! Tente um valor positivo!")
    else:
        print(f"Os divisores encontrados de {numero} são: \t")
    
    contador = 0
    
    for i in range (1, numero + 1):
        if numero % i == 0:
            print(f"{i}")
        contador += 1  
   
def ex7():
    
    print("__Introduza números inteiros positivos__\n")
    numeros = [] 
    mais_numero = "sim"
    
    while mais_numero.lower() == "sim":
        numero = int(input("\tIntroduza um numero: "))
        numeros.append(numero)
        mais_numero = str(input("\tPretende introduzir mais um numero (sim/nao)?: "))
        
    for numero in numeros:
        if numero <= 0:
            print(f"Introduziste um valor, {numero}, negativo ou nulo ! Tente um valor positivo!")
        else:
            print(f"Os divisores encontrados de {numero} são: \t")
            contador = 0
    
            for i in range (1, numero + 1):
                if numero % i == 0:
                    print(i)
                    contador += 1  
            print(f"\nO total de divisores: {contador}. ")
            print("+"*40)

#def ex8():

def ex9():
    
    print("\nIntroduza uma sequencia de número à sua escolha (0 para terminar):")
    numeros = [] 
    numero = int(input("\tIntroduza um numero: "))
       
    while numero != 0:
        numeros.append(numero)    
        numero = int(input("\tIntroduza outro um número (ou zero para terminar)?: "))
    print(f"\nPara a sequência de inteiros,{numeros}, foram identificados: \n") 
       
    if len(numeros) == 0:
        print("Campo vazio, sem números válidos introduzidos")
    else:
        maximo = max(numeros)
        posicao = numeros.index(maximo)+1
        tamanho = len(numeros)
        
        print(f"\tMáximo:                   {maximo}")
        print(f"\tPosição:                  {posicao}")
        print(f"\tTamanho da sequência:     {tamanho} \n")
    
def ex10():
                
        










def ex15():
    print("Introduza 5 números inteiros:")

    for i in range(1, 6):  # 5 números

        num = int(input(f"Número {i}: "))

        if num < 2:
            # "Um número primo é um número inteiro maior que 1 que tem exatamente dois divisores positivos: 1 e ele próprio."
            print(f"{num} não é primo.")
        else:
            primo = True
            for j in range(2, int(num**0.5) + 1):   # Testar até sqrt(num): 36 = 4 × 9 → 4 < √36 < 9
                if num % j == 0:
                    primo = False
                    break

                print(f"{num} é primo.") if primo else print(f"{num} não é primo.")





pass
#ex1()
#ex2()
#ex3()
#ex4()
#ex5()
#ex6()
#ex7()
#ex8()
#ex9()
ex10()

#ex15()