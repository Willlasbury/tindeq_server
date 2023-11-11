from pydantic import BaseModel

class WeightRes(BaseModel):
    type: int
    weights: object