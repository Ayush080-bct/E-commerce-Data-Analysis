import os
import joblib
import pandas as pd
from config import DATA_PATH,KMEANS_PATH,SCALER_PATH

class DataStore:
    "holds the rfm dataframe (with cluster  labels attached) plus the trained Scaler/Kmeans model, loaded once at api startup"

    def __init__(self)->None:
        self.rfm : pd.DataFrame | None=None
        self.scaler = None
        self.kmeans = None
        self.segment_map : dict[int, str] = {}

    def load(self)->None:
        if not os.path.exists(DATA_PATH):
            raise FileNotFoundError(f"Missing data file: {DATA_PATH}")
        if not os.path.exists(SCALER_PATH) or not os.path.exists(KMEANS_PATH):
            raise FileNotFoundError(
                "Missing model file in models/ . run the clustering notebook"
                "and joblib.dump th scaler + kmeans model first"
            )

        df = pd.read_csv(DATA_PATH)
        scaler = joblib.load(SCALER_PATH)
        kmeans = joblib.load(KMEANS_PATH)

        features = df[["Recency","Frequency","Monetory"]]
        df["Cluster"] = kmeans.predict(scaler.transform(features))

        segment_map = (
            df.groupby("Cluster")["segment"]
            .agg(lambda s: s.value_counts().idxmax())
            .to_dict()
        )

        self.rfm = df
        self.scaler = scaler
        self.kmeans = kmeans
        self.segment_map = segment_map

    @property
    def is_loaded(self) -> bool:
        return self.rfm is not None
    
store= DataStore()

def get_store() -> DataStore:
    """Fastapi dependency - lets route function declare `store: DataStore = Depends(get_store)`."""
    return store
        
