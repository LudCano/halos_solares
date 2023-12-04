import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros

r_ice = 0.004
r_water = 0.013
n_ice = 1.309
n_water = 1.333
ang_min = 22.5
ang_max = 100

# Generar los rayos

rays = np.random.uniform([-1, -1, 0], [1, 1, 1], size=(500000, 3))

# Interpolar los rayos a través de la atmósfera

rays = rays + np.random.normal(scale=0.001, size=rays.shape)
rays = rays / np.linalg.norm(rays, axis=-1, keepdims=True)

# Calcular la refracción de los rayos

for i in range(len(rays)):
    if rays[i, 2] > 0:
        rays[i, 2] = rays[i, 2] - r_ice
        for j in range(10):
            k = np.sin(rays[i, 2]) / n_ice
            rays[i, 2] = np.sqrt(k**2 - 1)
            if k * rays[i, 2] > 0:
                rays[i, 2] = k * rays[i, 2]
                break
    else:
        rays[i, 2] = rays[i, 2] + r_water
        for j in range(10):
            k = np.sin(rays[i, 2]) / n_water
            rays[i, 2] = np.sqrt(k**2 - 1)
            if k * rays[i, 2] < 0:
                rays[i, 2] = k * rays[i, 2]
                break

# Calcular el color de los rayos

colors = np.zeros(rays.shape[:2])
for i in range(len(rays)):
    ang = np.arcsin(rays[i, 2]) / np.pi * 180
    if ang > ang_min and ang < ang_max:
        colors[i] = plt.cm.Spectral(ang / (ang_max - ang_min))

# Dibujar los rayos

plt.scatter(rays[:, 0], rays[:, 1], c=colors, s=1)
plt.show()
