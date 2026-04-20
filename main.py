import numpy as np 
import matplotlib.pyplot as plt
from matriztransformacao import identidade, translacao, escala, rotacao_x, rotacao_y, rotacao_z
from testecodigo import criar_cilindro
import menu 
from visualizacao import desenhar 

vertices = criar_cilindro()
M_modelo = identidade()

print("Bem-vindo(a) à pipeline de visualização 3D!")

while True:
    print("\nMenu Principal:")
    print("1. Manipular o objeto")
    print("2. Manipular a câmera (não implementado)")
    print("3. Modificar projeção (não implementado)")
    print("4. Modificar mapeamento (não implementado)")
    print("5. Visualizar objeto")
    print("0. Sair")

    op = int(input("Escolha: "))

    if op == 1:
        sub = menu.menu_objeto()

        if sub == 1:
            tx = float(input("tx: "))
            ty = float(input("ty: "))
            tz = float(input("tz: "))
            M_modelo = translacao(tx, ty, tz) @ M_modelo

        elif sub == 2:
            sx = float(input("sx: "))
            sy = float(input("sy: "))
            sz = float(input("sz: "))
            M_modelo = escala(sx, sy, sz) @ M_modelo

        elif sub == 3:
            ang = float(input("Ângulo X: "))
            M_modelo = rotacao_x(ang) @ M_modelo

        elif sub == 4:
            ang = float(input("Ângulo Y: "))
            M_modelo = rotacao_y(ang) @ M_modelo

        elif sub == 5:
            ang = float(input("Ângulo Z: "))
            M_modelo = rotacao_z(ang) @ M_modelo

    elif op == 5:
        transformado = M_modelo @ vertices
        desenhar(transformado)

    elif op == 0:
        break