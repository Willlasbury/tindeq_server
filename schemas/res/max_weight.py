from pydantic import BaseModel
import datetime

class MaxWeightRes(BaseModel):
    id: int
    created_at: datetime.datetime
    weight: float
