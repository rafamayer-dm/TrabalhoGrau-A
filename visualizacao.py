import numpy as np 
import matplotlib.pyplot as plt
from matriztransformacao import identidade, translacao, escala, rotacao_x, rotacao_y, rotacao_z, geraMatrizCamera, projecaoPerspectiva
from testecodigo import criar_cilindro


def desenhar(vertices):
    # Divisão perspectiva
    x = vertices[0] / vertices[3]
    y = vertices[1] / vertices[3]

    plt.figure(figsize=(8, 8))

    # separar topo e base
    x_topo = x[::2]
    y_topo = y[::2]

    x_base = x[1::2]
    y_base = y[1::2]

    # fechar círculos
    x_topo = np.append(x_topo, x_topo[0])
    y_topo = np.append(y_topo, y_topo[0])

    x_base = np.append(x_base, x_base[0])
    y_base = np.append(y_base, y_base[0])

    # desenhar topo e base
    plt.plot(x_topo, y_topo, 'b-', linewidth=2, label='Topo')
    plt.plot(x_base, y_base, 'r-', linewidth=2, label='Base')

    # ligar topo e base
    for i in range(len(x_topo) - 1):
        plt.plot(
            [x_topo[i], x_base[i]],
            [y_topo[i], y_base[i]],
            'g-', linewidth=1, alpha=0.6
        )

    plt.title("Cilindro")
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.show()


def mudarCamera(camx, camy, camz, camrx, camry, camrz):
    M_camera = geraMatrizCamera(camx, camy, camz, camrx, camry, camrz)
    return M_camera

def mudarProjecao(fov, aspect, near, far):
    M_projecao = projecaoPerspectiva(fov, aspect, near, far)
    return M_projecao

