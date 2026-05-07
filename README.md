````md
# 🎵 Proyecto 1 - Predicción de Popularidad de Canciones

## 📌 Descripción del proyecto

Este proyecto tiene como objetivo predecir la popularidad de canciones de Spotify utilizando técnicas de Machine Learning basadas en modelos de árboles y ensambles.

A partir de diferentes características de audio de las canciones, el modelo estima un valor de popularidad entre 0 y 100.

El proyecto incluye:

- Exploración y análisis de datos
- Preprocesamiento
- Entrenamiento y calibración del modelo
- Evaluación del desempeño
- Despliegue de una API REST en la nube

---

# 📂 Dataset

El conjunto de datos contiene información de canciones de Spotify pertenecientes a múltiples géneros musicales.

## Variables relevantes

- `duration_ms`
- `danceability`
- `energy`
- `loudness`
- `speechiness`
- `acousticness`
- `instrumentalness`
- `liveness`
- `valence`
- `tempo`
- `track_genre`
- entre otras

## Variable objetivo

- `popularity`

---

# ⚙️ Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask
- Gunicorn
- Railway
- GitHub

---

# 🧠 Modelo de Machine Learning

Se utilizó un modelo de regresión basado en árboles:

## Modelo seleccionado

```python
RandomForestRegressor
````

El modelo fue seleccionado debido a:

* Su capacidad para capturar relaciones no lineales
* Robustez frente a outliers
* Buen desempeño con variables categóricas codificadas
* Reducción de sobreajuste mediante ensamble de árboles

---

# 🔧 Calibración de hiperparámetros

Se calibraron los siguientes hiperparámetros utilizando validación cruzada (`cv=5`) y RMSE como métrica de evaluación:

| Hiperparámetro   | Valor seleccionado |
| ---------------- | ------------------ |
| max_depth        | 80                 |
| min_samples_leaf | 2                  |
| n_estimators     | 300                |

---

# 📊 Métrica utilizada

Para evaluar el desempeño del modelo se utilizó:

```python
RMSE (Root Mean Squared Error)
```

Esta métrica permite penalizar con mayor peso los errores grandes y es adecuada para problemas de regresión.

---

# 🛠️ Preprocesamiento de datos

Durante el preprocesamiento se realizaron las siguientes actividades:

* Eliminación de variables de alta cardinalidad:

  * `track_id`
  * `artists`
  * `album_name`
  * `track_name`

* Conversión de variables booleanas a formato numérico

* División del dataset:

  * 80% entrenamiento
  * 20% validación

* Codificación One-Hot Encoding para variables categóricas:

  * `track_genre`
  * `key`
  * `time_signature`

El preprocesamiento fue ajustado únicamente sobre el conjunto de entrenamiento para evitar fuga de información.

---

# ☁️ API desplegada

La API REST fue desarrollada con Flask y desplegada en Railway.

## URL pública

```bash
https://proyecto1-txzq-production.up.railway.app
```

---

# 🚀 Endpoint de predicción

## Endpoint

```bash
POST /predict
```

## URL completa

```bash
https://proyecto1-txzq-production.up.railway.app/predict
```

---

# 📥 Ejemplo de request

```json
{
  "duration_ms": 200000,
  "explicit": 1,
  "danceability": 0.7,
  "energy": 0.8,
  "key": 5,
  "loudness": -5,
  "mode": 1,
  "speechiness": 0.05,
  "acousticness": 0.2,
  "instrumentalness": 0.0,
  "liveness": 0.1,
  "valence": 0.6,
  "tempo": 120,
  "time_signature": 4,
  "track_genre": "pop"
}
```

---

# 📤 Ejemplo de respuesta

```json
{
  "predicted_popularity": 36.57
}
```

---

# 📁 Estructura del proyecto

```bash
├── app.py
├── model.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
└── notebooks/
```

---

# ▶️ Ejecución local

## 1. Clonar repositorio

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
```

---

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3. Ejecutar aplicación

```bash
python app.py
```

---

# 📌 Resultados

El modelo logró capturar relaciones complejas entre las características musicales y la popularidad de las canciones, obteniendo un desempeño adecuado sobre el conjunto de validación.

El despliegue de la API permitió disponibilizar el modelo en la nube para realizar predicciones en tiempo real.

---

# ✅ Conclusiones

* Los modelos basados en árboles demostraron ser adecuados para este problema debido a la naturaleza no lineal de los datos.
* Variables como `track_genre`, `energy` y `danceability` aportaron información predictiva relevante.
* La calibración de hiperparámetros permitió mejorar el desempeño y la capacidad de generalización del modelo.
* El despliegue en Railway permitió disponibilizar el modelo mediante una API pública accesible desde cualquier entorno.

---



Proyecto desarrollado para el curso de Machine Learning.

