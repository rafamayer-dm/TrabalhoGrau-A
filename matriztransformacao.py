import numpy as np
import matplotlib.pyplot as plt

def identidade():
    return np.eye(4)

def translacao(tx, ty, tz):
    T = np.eye(4)
    T[0, 3] = tx
    T[1, 3] = ty
    T[2, 3] = tz
    return T

def escala(sx, sy, sz):
    S = np.eye(4)
    S[0, 0] = sx
    S[1, 1] = sy
    S[2, 2] = sz
    return S

def rotacao_x(theta):
    t = np.radians(theta)
    R = np.eye(4)
    R[1,1] = np.cos(t)
    R[1,2] = -np.sin(t)
    R[2,1] = np.sin(t)
    R[2,2] = np.cos(t)
    return R

def rotacao_y(theta):
    t = np.radians(theta)
    R = np.eye(4)
    R[0,0] = np.cos(t)
    R[0,2] = np.sin(t)
    R[2,0] = -np.sin(t)
    R[2,2] = np.cos(t)
    return R

def rotacao_z(theta):
    t = np.radians(theta)
    R = np.eye(4)
    R[0,0] = np.cos(t)
    R[0,1] = -np.sin(t)
    R[1,0] = np.sin(t)
    R[1,1] = np.cos(t)
    return R
