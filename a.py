import numpy as np
import matplotlib.pyplot as plt

# Parámetros
alto, ancho = 5, 5
bandas = 301

# Simular un espectro base (por ejemplo, absorción creciente)
espectro = np.linspace(0.2, 0.8, bandas)

# Nivel de ruido (relativo)
desv_relativa = .1  # 2% de variación

# Crear matriz hiperespectral vacía
imagen_hiper = np.zeros((alto, ancho, bandas))

# Llenar cada píxel con espectro + ruido
for i in range(alto):
    for j in range(ancho):
        ruido = np.random.normal(loc=0.0, scale=desv_relativa, size=bandas)
        espectro_pixel = espectro * (1 + ruido)
        imagen_hiper[i, j, :] = np.clip(espectro_pixel, 0, 1)

# Verificar el espectro promedio de toda la imagen
espectro_promedio = imagen_hiper.mean(axis=(0, 1))

plt.figure(figsize=(8, 4))
plt.plot(espectro, label="Espectro original")
plt.plot(espectro_promedio, label="Promedio en la imagen", linestyle='--')
plt.xlabel("Índice de banda")
plt.ylabel("Intensidad")
plt.legend()
plt.title("Comparación de espectros")
plt.grid(True)
plt.show()

# Visualizar la imagen en pseudo-RGB (elige bandas aproximadas)
# Por ejemplo: banda 60 ~ R, 30 ~ G, 10 ~ B
r_band = 60
g_band = 30
b_band = 10

rgb = np.stack([
    imagen_hiper[:, :, r_band],
    imagen_hiper[:, :, g_band],
    imagen_hiper[:, :, b_band]
], axis=2)

# Normalizar para que los valores estén entre 0 y 1
rgb_min = rgb.min()
rgb_max = rgb.max()
rgb_norm = (rgb - rgb_min) / (rgb_max - rgb_min)

plt.figure(figsize=(5, 5))
plt.imshow(rgb_norm)
plt.title(f"Composición RGB aproximada (bandas {r_band}, {g_band}, {b_band})")
plt.axis("off")
plt.show()

# Visualizar banda individual (ejemplo: banda 50)
banda_elegida = 50
plt.figure(figsize=(5, 5))
plt.imshow(imagen_hiper[:, :, banda_elegida], cmap='gray')
plt.title(f"Mapa de intensidad en banda {banda_elegida}")
plt.colorbar(label='Intensidad')
plt.axis("off")
plt.show()