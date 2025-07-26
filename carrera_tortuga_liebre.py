import numpy as np
import matplotlib.pyplot as plt
import threading

fondo = np.load("bosque.npy")
tortuga = np.load("tortuga.npy")
liebre = np.load("liebre.npy")

def procesar_kernel_en_fondo(fondo_frame, kernel, fila, col, num_hilos):
    alto, ancho, _ = kernel.shape
    fondo_recorte = fondo_frame[fila:fila+alto, col:col+ancho]

    def procesar_franja(inicio, fin):
        for i in range(inicio, fin):
            alpha = kernel[i, :, 3:4] / 255.0
            mezcla = (alpha * kernel[i, :, :3] + (1 - alpha) * fondo_recorte[i, :, :3]).astype(np.uint8)
            fondo_recorte[i, :, :3] = mezcla
            fondo_recorte[i, :, 3] = 255

    paso = alto // num_hilos
    hilos = [
        threading.Thread(target=procesar_franja, args=(i * paso, alto if i == num_hilos - 1 else (i + 1) * paso))
        for i in range(num_hilos)
    ]

    for h in hilos: h.start()
    for h in hilos: h.join()

def animar_carrera(fondo_rgba, tortuga, liebre, f_tortuga, f_liebre, paso_t, paso_l, frames_t, frames_l, hilos):
    alto_t, alto_l = tortuga.shape[0], liebre.shape[0]
    fila_t, fila_l = f_tortuga - alto_t, f_liebre - alto_l
    total_frames = max(frames_t, frames_l)

    for frame in range(total_frames):
        fondo_frame = fondo_rgba.copy()
        col_t, col_l = frame * paso_t, frame * paso_l

        if frame < frames_t and col_t + tortuga.shape[1] < fondo_rgba.shape[1]:
            procesar_kernel_en_fondo(fondo_frame, tortuga, fila_t, col_t, hilos)

        if frame < frames_l and col_l + liebre.shape[1] < fondo_rgba.shape[1]:
            procesar_kernel_en_fondo(fondo_frame, liebre, fila_l, col_l, hilos)

        plt.imshow(fondo_frame)
        plt.axis("off")
        plt.title(f"Carrera - Frame {frame}")
        plt.pause(0.00001)

    plt.close()

animar_carrera(fondo_rgba=fondo, tortuga=tortuga, liebre=liebre, f_tortuga=2191, f_liebre=2421, paso_t=300, paso_l=600, frames_t=16, frames_l=8, hilos=4)
