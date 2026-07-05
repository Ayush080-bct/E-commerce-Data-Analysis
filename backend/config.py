import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "rfm.csv"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
KMEANS_PATH = BASE_DIR / "models" / "kmeans.pkl"