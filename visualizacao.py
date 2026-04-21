import numpy as np 
import matplotlib.pyplot as plt
from matriztransformacao import identidade, translacao, escala, rotacao_x, rotacao_y, rotacao_z, geraMatrizCamera
from testecodigo import criar_cilindro

def desenhar(vertices):
    # Normalizar coordenadas homogêneas
    x = vertices[0] / vertices[3]
    y = vertices[1] / vertices[3]
    z = vertices[2] / vertices[3]

    # Vista frontal - mostrar cilindro de frente
    x2d = x
    y2d = y + z  # z controla a separação vertical (topo acima, base abaixo)

    plt.figure(figsize=(8, 8))
    
    # Separar topo e base (alternados)
    x_topo = x[::2]  # índices pares
    y_topo = y[::2]
    z_topo = z[::2]
    
    x_base = x[1::2]  # índices ímpares
    y_base = y[1::2]
    z_base = z[1::2]
    
    # Vista frontal
    x2d_topo = x_topo
    y2d_topo = z_topo + y_topo * 0.4
    
    x2d_base = x_base
    y2d_base = z_base + y_base * 0.4
    
    # Desenhar círculos (topo e base fechados)
    x2d_topo_fechado = np.append(x2d_topo, x2d_topo[0])
    y2d_topo_fechado = np.append(y2d_topo, y2d_topo[0])
    
    x2d_base_fechado = np.append(x2d_base, x2d_base[0])
    y2d_base_fechado = np.append(y2d_base, y2d_base[0])
    
    # Desenhar as arestas do cilindro
    plt.plot(x2d_topo_fechado, y2d_topo_fechado, 'b-', linewidth=2.5, label='Topo')
    plt.plot(x2d_base_fechado, y2d_base_fechado, 'r-', linewidth=2.5, label='Base')
    
    # Conectar topo com base (linhas verticais)
    for i in range(0, len(x2d_topo), 2):  # desenha cada 2 linhas para clareza
        plt.plot([x2d_topo[i], x2d_base[i]], [y2d_topo[i], y2d_base[i]], 'g-', linewidth=1.5, alpha=0.7)
    
    plt.title("Cilindro", fontsize=14)
    plt.xlim(x2d_topo.min() - 0.5, x2d_topo.max() + 0.5)
    plt.ylim(y2d_topo.min() - 0.5, y2d_topo.max() + 0.5)
    plt.grid()
    plt.axis('equal')
    plt.legend()
    plt.show()

def mudarCamera(camx, camy, camz, camrx, camry, camrz):
    M_camera = geraMatrizCamera(camx, camy, camz, camrx, camry, camrz)
    return M_camera

