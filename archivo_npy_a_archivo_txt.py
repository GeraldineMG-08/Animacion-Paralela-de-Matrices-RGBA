import numpy as np

matriz = np.load("bosque.npy")
pixels = matriz.reshape(-1, 4)

visibles = pixels[pixels[:, 3] > 0]
primeros = visibles[:300]

with open("pixeles_visibles.txt", "w") as f:
    f.write("Primeros 300 visibles (RGBA):\n")
    for fila in primeros:
        valores = [int(x) for x in fila]  
        f.write(f"{valores}, ")


print("Archivo 'pixeles_visibles.txt' guardado correctamente.")
