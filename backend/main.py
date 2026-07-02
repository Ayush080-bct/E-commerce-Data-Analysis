"""
Customer segementation API 
"""

from pathlib import Path
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "rfm.csv"
SCALER_PATh = BASE_DIR / "models" / "scaler.pkl"
KMEANS_PATH = BASE_DIR / "models" / "kmeans.pkl"

app = FastAPI(title="Customer Segementation API",version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",   # local Streamlit dev server
        "https://my-streamlit-app.com"  # deployed Streamlit app
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # restrict to what you actually use
    allow_headers=["*"],            # or specify headers if needed
)

# type hints
_rfm: pd.DataFrame | None=None
_scaler = None
_kmeans = None
_seg_map: dict | None = None

@app.get('/')
def root():
    data = {"messgae":"Backend run sucessfully","status":"ok"}
    return JSONResponse(content=data,status_code=200)