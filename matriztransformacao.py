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

def geraMatrizCamera (camx, camy, camz, camrx, camry, camrz):
 
    t = np.array([
        [1, 0, 0, -camx],
        [0, 1, 0, -camy],
        [0, 0, 1, -camz],
        [0, 0, 0, 1]
    ])

    camrx = np.radians(camrx)
    camry = np.radians(camry)
    camrz = np.radians(camrz)

    #Matrizes de rotação
    Rx = np.array([ [1,     0,                  0,              0],
                    [0,     np.cos(-camrx),    -np.sin(-camrx), 0],
                    [0,     np.sin(-camrx),    np.cos(-camrx),  0],
                    [0,     0,                  0,              1]])
    
    Ry = np.array([ [np.cos(camry),    0, np.sin(camry),     0],
                    [0,                 1, 0,                  0],
                    [-np.sin(camry),   0, np.cos(camry),     0],
                    [0,                 0, 0,                  1]])
    
    Rz = np.array([ [np.cos(-camrz),   -np.sin(-camrz),     0,  0],
                    [np.sin(-camrz),    np.cos(-camrz),     0,  0],
                    [0,                 0,                  1,  0],
                    [0,                 0,                  0,  1]])
        
    combinacao = Rz @ Ry @ Rx @ t

    return combinacao

def projecaoPerspectiva(fovy, aspect, znear, zfar):
    fovy = np.radians(fovy)

    a = 1/(np.tan(fovy/2)*aspect)
    b = 1/np.tan(fovy/2)
    c = (zfar+znear)/(znear-zfar)
    d = (2*zfar*znear)/(znear-zfar)

    p = np.array([[a, 0, 0,  0],
                  [0, b, 0,  0],
                  [0, 0, c,  d],
                  [0, 0, -1, 0]])
    
    return p




