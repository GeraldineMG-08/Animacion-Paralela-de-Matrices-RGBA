import numpy as np
import matplotlib.pyplot as plt

def mostrar_imagen(imagen, titulo=""):
    
    plt.imshow(imagen.astype(np.uint8))
    plt.title(titulo)
    plt.axis('off') 
    plt.show()
    print("Forma de la imagen:", imagen.shape)

kernel = np.load("liebre.npy")
mostrar_imagen(kernel)
