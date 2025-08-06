import math
import random

def calculadora (a,b, operacao):
    if operacao == "+":
        resultado = a+b
        print(f"O resultado da soma e: {resultado}")
    elif operacao == "*":
        resultado = a*b
        print(f"O resultado da multiplicacao e: {resultado}")
    elif operacao == "/" and b!=0:
        resultado = a/b
        print(f"O resultado da divisao e: {resultado}")  
    elif operacao == "-":
        resultado = a-b
        print(f"O resultado da subtracao e: {resultado}")
    else:
        print("Operacao invalida, tente usar (+,-,+,*)!")
    return resultado    

num1=float(input("introduza um numero: "))
operacao = str(input("escolha a sua operacao (+,-,/,*): "))  
num2=float(input("introduza outro numero: "))

resultado = calculadora(num1, num2, operacao)


def converter_temperatura (valor, escala ='C'):

    if escala.lower() == "f":
        Fahrenheit =(valor*9/5)+32
        print (f"{valor:.2f} graus Celsius e igual {Fahrenheit:.2f} graus Fahrenheit") 
    elif escala.lower() == "c":
        celsius = (valor-32) *5/9
        print (f"{valor:.2f} graus Fahrenheit e igual {celsius:.2f} graus Celsius")   
    else:
        print("Escala inválidas, tente novamente com 'c' e 'f'")
        
valor = float(input("Qual é a temperatura que deseja converter: "))
escala = str(input("Insira (c) se deseja converter para Celsius ou para Fahrenheit (f): "))
resultado = converter_temperatura(valor, escala)


def validar_email(email): 
    
    if len(email) < 6:
        print("Email inválido! Pois, é muito curto!\n")
        return False
    if "@" not in email:
        print("Email inválido! Use '@'\n")
        return False
    dp_arroba = email.index("@")
    if "." not in email[dp_arroba+1:]:
        print("Email inválido! Use o ponto '.' depois do arroba\n")
        return False
    return True

list_emails = ["paulovundi@gmail.com", "paulo@gmailcom", "paulovundi!com", "paulovundi@com"]

for email in list_emails:
    if validar_email(email):
        print(f"O email '{email}' é válido!\n")
    else:
        print(f"O email '{email}' inserido não é válido!\n")


#def media_notas (*notas):

def menu_agenda():
    nome=input("Digite o teu nome: ")
    print(f"Seja Bem-Vindo a SmartAgenda: {nome}\n")
    print("Selecione uma das opções a realizar:", "\n\tOpcao-1 Adicionar Tarefas", "\n\tOpcao-2 Remover Tarefas", "\n\tOpcao-3 Listas de tarefas", "\n\tOpcao-0 Para sair")
    
def agenda ():
    menu_agenda()
    listar_tarefas = []
    adicionar_tarefa = "sim"
    
    while adicionar_tarefa.lower() == "sim":
        tipo_tarefa = input(f"\nAdicione uma nova tarefa {nome}: ")
        listar_tarefas.append(tipo_tarefa)
                      
        print(f"\n{nome}, as tarefas na tua agenda sao: \t")
        for i, tarefa in enumerate(listar_tarefas): 
            print(f"{i+1}. {tipo_tarefa}") 
        
        adicionar_tarefa = input(f"Deseja adicionar outra tarefa {nome}?")    
        
        eliminar_tarefa = input("\nDeseja remover alguma tarefa? (sim/nao): ").lower().upper()
        while eliminar_tarefa.lower() == "sim":
            try:
                indice_eliminar = int(input("Digite o numero da tarefa que deseja remover: ")) - 1  
                if 0 <= indice_eliminar < len(listar_tarefas): 
                    tarefa_eliminada = listar_tarefas.pop(indice_eliminar) 
                    print(f"Tarefa '{tarefa_eliminada}' removida!")
                else:
                    print("Indice invalido. A tarefa nao foi removida.")
            except ValueError:
                print("Entrada invalida. Por favor, digite um numero.")
            if not listar_tarefas:
                print("Agenda sem tarefas")
                break
            eliminar_tarefa = input("Deseja remover outra tarefa? (sim/nao): ").lower()
    print("\nAgenda finalizada.")

agenda ()
        
def gestor_contactos():
    nome =input("Digite o teu nome: ")
    print(f"Seja Bem-Vindo ao GestContactos: {nome}\n")
    #print("Selecione uma das opções a realizar:", "\n\tOpcao-1 Adicionar contactos", "\n\tOpcao-2 Remover contactos", "\n\tOpcao-3 Listas de contactos", "\n\tOpcao-0 Para sair")

    listar_contactos = []
    adicionar_contactos = "sim"
    
    while adicionar_contactos.lower() == "sim":
        tipo_contacto = input(f"\nAdicione um novo contacto {nome}: ")
        listar_contactos.append(tipo_contacto)
                      
        print(f"\n{nome}, os contactos na tua agenda sao: \t")
        for i, contactos in enumerate(listar_contactos): 
            print(f"{i+1}. {tipo_contacto}") 
        
        adicionar_contactos = input(f"Deseja adicionar outro contacto, {nome}?")    
        
        eliminar_contactos = input("\nDeseja remover algum contacto? (sim/nao): ").lower().upper()
        while eliminar_contactos.lower() == "sim":
            try:
                indice_eliminar = int(input("Digite o numero do contacto que deseja remover: ")) - 1  
                if 0 <= indice_eliminar < len(listar_contactos): 
                    contacto_eliminado = listar_contactos.pop(indice_eliminar) 
                    print(f"Contacto'{contacto_eliminado}' removido!")
                else:
                    print("Indice invalido. O contacto nao foi removido.")
            except ValueError:
                print("Entrada invalida. Por favor, digite um numero.")
            if not listar_contactos:
                print("GestContactos sem contactos")
                break
            eliminar_contactos = input("Deseja remover outro contacto? (sim/nao): ").lower()
    print("\nGestContactos finalizado!")

gestor_contactos()
    




  
    
pass
#calculadora()
#converter_temperatura()
#validar_email()
#media_notas()
#agenda ()
#gestor_contactos()