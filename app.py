from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "API funcionando"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return "Endpoint activo. Usa POST para predecir."

    data = request.json
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    return jsonify({"predicted_popularity": float(pred)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
