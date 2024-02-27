from pydantic import BaseModel

class StyleData(BaseModel):
    edge_size_mm: int
    grip: str
    hand: str
    index: bool
    middle: bool
    ring: bool
    pinky: bool