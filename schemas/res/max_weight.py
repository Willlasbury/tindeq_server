from pydantic import BaseModel
import datetime
from models.styles import Style

class MaxWeightRes(BaseModel):
    weight_kg: float
    style: Style

