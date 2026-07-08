import pandas as pd
from fastapi import APIRouter, Depends, HTTPException
from store import DataStore,get_store
from schemas import (
    CustomerResponse,
    OverviewResponse,
    PredictRequest,
    PredictResponse
)
router=APIRouter()
@router.get("/health")
def health(store: DataStore = Depends(get_store)):#Depends(get_store) is part of FastAPI’s dependency injection system
    #Depends() tells FastAPI: “this function needs something injected before it runs.”
    return {
        "Status":"Ok",
        "customers_loaded":0 if not store.is_loaded else len(store.rfm),
    }
@router.get("/overview",response_model=OverviewResponse)
def overview(store : DataStore = Depends(get_store)):#FastAPI will automatically call get_store() and pass its return value (store) into your overview function.
    df = store.rfm 
    seg_counts=df["segment"].value_counts().to_dict()
    revenue_by_segment = df.groupby("segment")["Monetory"].sum().round(2).to_dict()
    summary=(
        df.groupby("segment")
        .agg(
            Customers=("CustomerID", "count"),
            Avg_Recency=("Recency", "mean"),
            Avg_Frequency=("Frequency", "mean"),
            Avg_Monetary=("Monetory", "mean"),
        )
        .round(1)
        .reset_index()
        .to_dict(orient="records")
    )
    return OverviewResponse(
        total_customers=len(df),
        total_revenue=round(float(df["Monetory"].sum()), 2),
        avg_order_value=round(float(df["Monetory"].mean()), 2),
        num_segments=int(df["segment"].nunique()),
        segment_counts=seg_counts,
        revenue_by_segment=revenue_by_segment,
        summary=summary,
    )
@router.get("/cluster/scatter")
def cluster_scatter(store : DataStore = Depends(get_store)):
    df = store.rfm[["CustomerID","Recency","Frequency","Monetory","Cluster","segment"]]
    return df.to_dict(orient="records")
@router.get("/customers")
def list_customers(store:DataStore=Depends(get_store)):
    return sorted(store.rfm["CustomerID"].astype(str).tolist())

