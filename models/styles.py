from pydantic import BaseModel
class Style(BaseModel):
    def __init__(self, edge_size_mm, grip, hand, index, middle, ring, pinky) -> None:
        self.edge_size_mm = edge_size_mm
        self.grip = grip
        self.hand = hand
        self.index = index
        self.middle = middle
        self.ring = ring
        self.pinky = pinky
