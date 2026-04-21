
import numpy as np
import matplotlib.pyplot as plt

def menu_objeto():
    print("\nMenu Objeto:")
    print("1. Translação")
    print("2. Escala")
    print("3. Rotação X")
    print("4. Rotação Y")
    print("5. Rotação Z")
    opcao = int(input("Escolha: "))
    return opcao

def menu_camera():
    print("\nMenu Camera:")
    print("1. Translação")
    print("2. Rotação X")
    print("3. Rotação Y")
    print("4. Rotação Z")
    escolha = int(input("Escolha: "))
    return escolha

def menu_projecao():
    print("\nMenu Projeção:")
    print("1. Perspectiva")
    print("2. Paralela")
    escolha = int(input("Escolha: "))
    return escolha
