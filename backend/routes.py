import pandas as pd
from fastapi import APIRouter, Depends, HTTPException
from backend.store import DataStore,get_store
from schemas import (
    CustomerResponse,
    OverviewResponse,
    PredictRequest,
    PredictResponse
)
router=APIRouter()
@router.get("/health")
def health(store: DataStore = Depends(get_store))
    return {
        "Status":"Ok",
        "customers_loaded":0 if not store.is_loaded else len(store.rfm),
    }
