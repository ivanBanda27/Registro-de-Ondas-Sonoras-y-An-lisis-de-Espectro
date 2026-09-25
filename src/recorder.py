"""
recorder.py
Graba audio desde el micrófono y lo guarda como archivo .wav
en la carpeta data/recordings/.
"""

import sounddevice as sd
from scipy.io.wavfile import write
import os

# --- Parámetros de grabación ---
DURACION = 3          # segundos
FS = 44100            # frecuencia de muestreo (Hz), estándar de audio
CANALES = 1            # 1 = mono, 2 = estéreo
NOMBRE_ARCHIVO = "grabacion.wav"

# Ruta de salida relativa a este script
CARPETA_SALIDA = os.path.join(os.path.dirname(__file__), "..", "data", "recordings")
os.makedirs(CARPETA_SALIDA, exist_ok=True)
RUTA_SALIDA = os.path.join(CARPETA_SALIDA, NOMBRE_ARCHIVO)


def grabar_audio(duracion=DURACION, fs=FS, canales=CANALES):
    """Graba audio del micrófono durante 'duracion' segundos."""
    print(f"Grabando {duracion} segundos... (habla, silba o reproduce el tono ahora)")
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=canales, dtype='int16')
    sd.wait()  # espera a que termine la grabación
    print("Grabación finalizada.")
    return audio


def guardar_audio(audio, ruta=RUTA_SALIDA, fs=FS):
    """Guarda el arreglo de audio como archivo .wav."""
    write(ruta, fs, audio)
    print(f"Archivo guardado en: {ruta}")


if __name__ == "__main__":
    audio = grabar_audio()
    guardar_audio(audio)