
import numpy as np
import matplotlib.pyplot as plt

def menu_objeto (opcao):
    if opcao == 1:
        print("Translação")
    elif opcao == 2: 
        print("Escala")
    elif opcao == 3 :
        print ("Rotação X")
    elif opcao == 4:
        print ("Rotação Y")
    elif opcao == 5:
        print ("Rotação Z")

opcao = int (input ("Escolha uma opção: \n 1 - Translação \n 2 - Escala \n 3 - Rotação X \n 4 - Rotação Y \n 5 - Rotação Z \n" ))
print (menu_objeto (opcao))