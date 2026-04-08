print ("Bem vindo(a) a pipeline de vizualização 3d!")
user_input = int (input ("Escolha uma das opções abaixo: "))

print("1. Manipular o objeto")
print("2. Manipular a câmera")
print("3. Modificar projeção")
print("4. Modificar mapeamento")
print("5. Visualizar objeto")


def menu (opcao):
    if opcao == 1:
        print("Manipulando objeto!")
    elif opcao == 2: 
        print("Manipulando camera!")
    elif opcao == 3 :
        print ("Modificando projeçao!")
    elif opcao == 4:
        print ("Modificando mapeamento!")
    elif opcao == 5:
        print ("Visualizando objeto!")

print (menu (user_input))