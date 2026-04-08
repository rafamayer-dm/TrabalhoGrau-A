import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# oiiiiii
fig = plt.figure()
ax = plt.axes(projection='3d')
x, y, z = np.indices((8,8,8))

cube1 = ( x < 3 ) & ( y < 3 ) & ( z < 3 ) 
cube2 = ( x >= 5 ) & ( y >= 5 ) & ( z >= 5 )

voxelarray = cube1 | cube2

fig, ax = plt.subplots (subplot_kw= {"projection": "3d"})
ax.voxels(voxelarray, facecolors="pink", edgecolor= "red")
ax.set (xlabel= "X", ylabel= "Y", zlabel= "Z")

plt.savefig("voxels.png")
print("Imagem salva como voxels.png")
