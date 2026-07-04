from pydantic import BaseModel


class PredictRequest(BaseModel):
    recency: float
    frequency: float
    monetary: float
 
 
class PredictResponse(BaseModel):
    cluster: int
    segment: str
 
 
class CustomerResponse(BaseModel):
    CustomerID: str
    Recency: float
    Frequency: float
    Monetary: float
    RFM_score: str
    segment: str
    cluster: int
    cluster_typical_segment: str


class OverviewResponse(BaseModel):
    total_customers: int
    total_revenue: float
    avg_order_value: float
    num_segments: int
    segment_counts: dict[str, int]
    revenue_by_segment: dict[str, float]
    summary: list[dict]