from pydantic import BaseModel
import datetime

class MaxWeightRes(BaseModel):
    weight_kg: float
    style: dict

