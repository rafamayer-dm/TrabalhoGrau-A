
import numpy as np
import matplotlib.pyplot as plt

def criar_cilindro(num_lados=20):
    vertices = []

    raio = 0.5

    # topo e base
    for i in range(num_lados):
        ang = 2 * np.pi * i / num_lados
        x = raio * np.cos(ang)
        y = raio * np.sin(ang)

        # topo (z = +0.5)
        vertices.append([x, y, 0.5, 1])

        # base (z = -0.5)
        vertices.append([x, y, -0.5, 1])

    arr = np.array(vertices)
    return arr.T