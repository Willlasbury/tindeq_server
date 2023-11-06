from pydantic import BaseModel

class weightData(BaseModel):
    type: str
    weights: list[float]