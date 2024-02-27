from pydantic import BaseModel
from typing import Literal


class StyleData(BaseModel):
    edge_size_mm: int
    grip: Literal["full", "half", "open"]
    hand: Literal["left", "right"]
    index: bool
    middle: bool
    ring: bool
    pinky: bool
