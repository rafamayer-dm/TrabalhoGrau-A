import numpy as np 
import matplotlib.pyplot as plt
from matriztransformacao import identidade, translacao, escala, rotacao_x, rotacao_y, rotacao_z
from testecodigo import criar_cilindro

def desenhar(vertices):
    x = vertices[0]
    y = vertices[1]

    plt.figure()
    plt.scatter(x, y)
    plt.title("Projeção simples (debug)")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.grid()
    plt.show()

desenhar(criar_cilindro(20))