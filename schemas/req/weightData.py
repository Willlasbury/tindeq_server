from pydantic import BaseModel
from schemas.req.styleData import StyleData

class WeightData(BaseModel):
    weight: float
    style: StyleData
