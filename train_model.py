"""Melatih model regresi linear untuk mengestimasi MPG jalan raya dari kapasitas mesin."""
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "mpg.csv"
MODEL_PATH = BASE_DIR / "model.joblib"
METRICS_PATH = BASE_DIR / "model_metrics.json"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset tidak ditemukan: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    needed = ["displ", "hwy"]
    missing_columns = [c for c in needed if c not in df.columns]
    if missing_columns:
        raise ValueError(f"Kolom wajib tidak ditemukan: {missing_columns}")
    data = df[needed].dropna().copy()
    X = data[["displ"]]
    y = data["hwy"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    result = {
        "observations_total": int(len(data)),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "intercept": float(model.intercept_),
        "coefficient_displ": float(model.coef_[0]),
        "r2": float(r2_score(y_test, pred)),
        "mae": float(mean_absolute_error(y_test, pred)),
        "mse": float(mean_squared_error(y_test, pred)),
        "rmse": float(np.sqrt(mean_squared_error(y_test, pred))),
    }
    joblib.dump(model, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print("Model berhasil dilatih dan disimpan.")
    print(f"Persamaan: hwy = {model.intercept_:.4f} + ({model.coef_[0]:.4f} x displ)")
    print(f"R-squared: {result['r2']:.4f}")
    print(f"RMSE: {result['rmse']:.4f} MPG")
    print(f"MAE: {result['mae']:.4f} MPG")


if __name__ == "__main__":
    main()
