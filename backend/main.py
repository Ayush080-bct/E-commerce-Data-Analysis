"""
Customer segementation API 
"""



from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException

from backend.routes import router
from backend.store import store

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

app.include_router(router)

@app.on_event("startup")
def startup():
    store.load()