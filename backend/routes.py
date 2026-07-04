import pandas as pd
from fastapi import APIRouter, Depends, HTTPException

from schemas import (
    CustomerResponse,
    OverviewResponse,
    PredictRequest,
    PredictResponse
)
