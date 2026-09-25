"""
time_plot.py
Lee un archivo .wav grabado y grafica la señal en el dominio del tiempo
(amplitud vs. tiempo).
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# --- Rutas ---
CARPETA_BASE = os.path.dirname(__file__)
RUTA_AUDIO = os.path.join(CARPETA_BASE, "..", "data", "recordings", "grabacion.wav")
CARPETA_FIGURAS = os.path.join(CARPETA_BASE, "..", "output", "figures")
os.makedirs(CARPETA_FIGURAS, exist_ok=True)
RUTA_FIGURA = os.path.join(CARPETA_FIGURAS, "time_plot.png")

# Ventana de zoom para medir el periodo (en segundos)
ZOOM_INICIO = 0.5       # segundo donde empieza el zoom
ZOOM_DURACION = 0.02    # 20 ms: suficiente para ver varios ciclos de un tono audible


def cargar_audio(ruta=RUTA_AUDIO):
    """Carga el archivo .wav y devuelve la frecuencia de muestreo y los datos."""
    fs, datos = read(ruta)
    # Si el audio es estéreo, tomamos solo un canal
    if datos.ndim > 1:
        datos = datos[:, 0]
    return fs, datos


def graficar_tiempo(fs, datos, zoom_inicio=ZOOM_INICIO, zoom_duracion=ZOOM_DURACION, guardar=True):
    """
    Grafica la señal de audio en el dominio del tiempo en dos paneles:
    1) la señal completa
    2) un zoom de 'zoom_duracion' segundos a partir de 'zoom_inicio',
       para poder medir el periodo visualmente.
    """
    duracion = len(datos) / fs
    tiempo = np.linspace(0, duracion, num=len(datos))

    # Índices del rango de zoom
    i_ini = int(zoom_inicio * fs)
    i_fin = int((zoom_inicio + zoom_duracion) * fs)
    i_fin = min(i_fin, len(datos))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

    # --- Panel 1: señal completa ---
    ax1.plot(tiempo, datos, linewidth=0.8)
    ax1.set_title("Señal de audio en el dominio del tiempo")
    ax1.set_xlabel("Tiempo (s)")
    ax1.set_ylabel("Amplitud")
    ax1.grid(True)
    # Marca el rango que se muestra en el zoom
    ax1.axvspan(tiempo[i_ini], tiempo[i_fin - 1], color="orange", alpha=0.3)

    # --- Panel 2: zoom para medir el periodo ---
    ax2.plot(tiempo[i_ini:i_fin], datos[i_ini:i_fin], marker="o", markersize=2, linewidth=1)
    ax2.set_title(f"Zoom ({zoom_duracion * 1000:.0f} ms) para medir el periodo")
    ax2.set_xlabel("Tiempo (s)")
    ax2.set_ylabel("Amplitud")
    ax2.grid(True)

    plt.tight_layout()

    if guardar:
        plt.savefig(RUTA_FIGURA, dpi=150)
        print(f"Gráfico guardado en: {RUTA_FIGURA}")

    plt.show()


if __name__ == "__main__":
    fs, datos = cargar_audio()
    graficar_tiempo(fs, datos)