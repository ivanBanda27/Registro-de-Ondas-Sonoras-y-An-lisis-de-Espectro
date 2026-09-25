"""
fft_analysis.py
Calcula la Transformada Rápida de Fourier (FFT) de la grabación de audio
y grafica el espectro de frecuencias (magnitud vs. frecuencia).
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq

# --- Rutas ---
CARPETA_BASE = os.path.dirname(__file__)
RUTA_AUDIO = os.path.join(CARPETA_BASE, "..", "data", "recordings", "grabacion.wav")
CARPETA_FIGURAS = os.path.join(CARPETA_BASE, "..", "output", "figures")
os.makedirs(CARPETA_FIGURAS, exist_ok=True)
RUTA_FIGURA = os.path.join(CARPETA_FIGURAS, "fft_spectrum.png")


def cargar_audio(ruta=RUTA_AUDIO):
    """Carga el archivo .wav y devuelve la frecuencia de muestreo y los datos."""
    fs, datos = read(ruta)
    if datos.ndim > 1:
        datos = datos[:, 0]
    return fs, datos


def calcular_fft(fs, datos):
    """
    Calcula la FFT de la señal y devuelve solo la mitad positiva
    del espectro (por simetría de la FFT de una señal real).
    """
    n = len(datos)
    fft_valores = fft(datos)
    fft_frecuencias = fftfreq(n, d=1 / fs)

    # Solo la mitad positiva del espectro
    mitad = n // 2
    frecuencias = fft_frecuencias[:mitad]
    magnitudes = np.abs(fft_valores[:mitad]) / n  # normalizado

    return frecuencias, magnitudes


def graficar_espectro(frecuencias, magnitudes, freq_max=2000, guardar=True):
    """
    Grafica el espectro de frecuencias.
    freq_max limita el eje x para enfocarse en frecuencias audibles relevantes.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(frecuencias, magnitudes, linewidth=0.8)
    plt.title("Espectro de frecuencias (FFT)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.xlim(0, freq_max)
    plt.grid(True)
    plt.tight_layout()

    if guardar:
        plt.savefig(RUTA_FIGURA, dpi=150)
        print(f"Gráfico guardado en: {RUTA_FIGURA}")

    plt.show()


def frecuencia_dominante(frecuencias, magnitudes):
    """Devuelve la frecuencia con mayor magnitud (el tono dominante)."""
    idx = np.argmax(magnitudes)
    return frecuencias[idx]


if __name__ == "__main__":
    fs, datos = cargar_audio()
    frecuencias, magnitudes = calcular_fft(fs, datos)
    graficar_espectro(frecuencias, magnitudes)

    f_dominante = frecuencia_dominante(frecuencias, magnitudes)
    print(f"Frecuencia dominante detectada: {f_dominante:.2f} Hz")