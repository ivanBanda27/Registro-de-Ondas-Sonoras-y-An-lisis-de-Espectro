
#  🎵 Registro de Ondas Sonoras y Análisis de Espectro

Proyecto de aula para la Universidad Tecnológica de Bolívar. Captura de ondas sonoras en el dominio del tiempo y análisis de frecuencias mediante la Transformada de Fourier (FFT) utilizando Python.

## 🔬 Sobre el Proyecto

Este proyecto forma parte de la asignatura Física Calor y Ondas de la Facultad de Ciencias Básicas de la Universidad Tecnológica de Bolívar. Consiste en el desarrollo de un script en Python capaz de interactuar con la tarjeta de sonido del computador para capturar señales acústicas reales (como notas musicales de instrumentos o diapasones), graficar su comportamiento temporal y descomponer la señal en su espectro de frecuencias utilizando análisis armónico.

## 📂 Estructura del Repositorio
```text
registro-espectro-sonido/
├──📁assets/         # Imágenes y gráficas de ejemplo (oscilación y FFT)
├──📁src/            # Código fuente principal en Python
├── requirements.txt # Librerías necesarias (numpy, scipy, matplotlib, sounddevice)
└── README.md       # Documentación del proyecto
```

## ⚙️ Requisitos Previos y Dependencias

Asegúrate de tener instalado **Python 3.8 o superior**. Las librerías principales utilizadas en el proyecto son:

*   `numpy` (cálculo numérico)
*   `scipy` (procesamiento de señales y FFT)
*   `matplotlib` (generación de gráficas)
*   `sounddevice` o `pyaudio` (captura de audio desde el micrófono)

Puedes instalar todas las dependencias ejecutando:

```bash
pip install -r requirements.txt
```
## 🚀 Instalación y Ejecución

Sigue estos pasos para clonar y ejecutar el programa en tu equipo local:

### 1. Clonar el repositorio
Abre tu terminal y ejecuta el siguiente comando:

```bash
git clone https://github.com/ivanBanda27/registro-espectro-sonido.git

cd registro-espectro-sonido
```
### 2. Instalar las dependencias
Instala las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```
### 3. Ejecutar el programa
Inicia la captura del sonido y el cálculo de la transformada de Fourier ejecutando el script principal:
```bash
python src/main.py
```
