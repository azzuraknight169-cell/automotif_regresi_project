"""Aplikasi Flask sederhana untuk prediksi efisiensi BBM berdasarkan kapasitas mesin."""
from pathlib import Path
import joblib
import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"
app = Flask(__name__)

# Latih model terlebih dahulu dengan menjalankan `python train_model.py`.
if not MODEL_PATH.exists():
    raise FileNotFoundError("model.joblib belum tersedia. Jalankan: python train_model.py")
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    displ_value = ""
    if request.method == "POST":
        displ_value = request.form.get("displ", "").strip()
        try:
            displ = float(displ_value)
            if not 1.6 <= displ <= 7.0:
                raise ValueError("Masukkan kapasitas mesin pada rentang data 1,6 sampai 7,0 liter.")
            prediction = float(model.predict(pd.DataFrame({"displ": [displ]}))[0])
        except ValueError as exc:
            error = str(exc) or "Input harus berupa angka yang valid."
    return render_template("index.html", prediction=prediction, error=error, displ_value=displ_value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
