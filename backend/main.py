"""
Customer segementation API 
"""



from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


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

def _load_everything():
    global _rfm , _scaler,_kmeans,_seg_map

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Missing data file : {DATA_PATH}")
    if not os.path.exists(SCALER_PATh) and not os.path.exists(KMEANS_PATH):
        raise FileNotFoundError(
            "Missing model files in model/. RUn the clustering notebook "
            "and joblib.dump the scaler + kmeans model first"
        )
    df =pd.read_csv(DATA_PATH)
    scaler = joblib.load(SCALER_PATh)
    kmeans = joblib.load(KMEANS_PATH)
