from PIL import Image
import numpy as np

def image_to_matrix(image_path, resolution):
    img = Image.open(image_path)
    img_resized = img.resize(resolution)
    img_rgba = img_resized.convert("RGBA")
    pixel_matrix = np.array(img_rgba, dtype=np.uint8)
    return pixel_matrix

image_path = "C:\\Users\\PC\\Downloads\\proyecto AP\\final\\fondo_bosque.jpg"
resolution = (5000, 3320) #columnas, filas
""" tortuga (642, 560)
    liebre (300, 500)
    bosque (5000, 3320)"""

pixel_matrix = image_to_matrix(image_path, resolution)

np.save("bosque.npy", pixel_matrix)

print("La matriz RGBA se ha guardado.")
