import numpy as np 
import matplotlib.pyplot as plt
from matriztransformacao import identidade, translacao, escala, rotacao_x, rotacao_y, rotacao_z, geraMatrizCamera
import menu
from testecodigo import criar_cilindro
from menu import menu_objeto, menu_camera
from visualizacao import desenhar 




vertices = criar_cilindro()
M_modelo = identidade()

# Estado inicial da câmera
camx = 0.0
camy = 0.0
camz = 0.0   

camrx = 0.0
camry = 0.0
camrz = 0.0

M_camera =geraMatrizCamera(camx, camy, camz, camrx, camry, camrz)

print("Bem-vindo(a) à pipeline de visualização 3D!")

while True:
    print("\nMenu Principal:")
    print("1. Manipular o objeto")
    print("2. Manipular a câmera")
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
            M_modelo =  escala(sx, sy, sz) @ M_modelo 

        elif sub == 3:
            ang = float(input("Ângulo X: "))
            M_modelo = rotacao_x(ang) @ M_modelo
            
        elif sub == 4:
            ang = float(input("Ângulo Y: "))
            M_modelo =  rotacao_y(ang) @ M_modelo 

        elif sub == 5:
            ang = float(input("Ângulo Z: "))
            M_modelo =  rotacao_z(ang) @ M_modelo 

    if op == 2:
        sub = menu.menu_camera()

        if sub == 1:
            camx = float(input("camx: "))
            camy = float(input("camy: "))
            camz = float(input("camz: "))

        elif sub == 2:
            camrx = float(input("Rot X (graus): "))
        
        elif sub == 3:
            camry = float(input("Rot Y (graus): "))
            
        elif sub == 4:
            camrz = float(input("Rot Z (graus): "))

        M_camera = geraMatrizCamera(camx, camy, camz, camrx, camry, camrz)



    elif op == 5:  
        V_modelo = M_modelo @ vertices
        V_camera = M_camera @ V_modelo
        desenhar(V_camera)


    elif op == 0:
        print("Encerrando...")
        break
