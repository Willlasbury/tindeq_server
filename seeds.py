from routes.weights import create_max_weight
from routes.tindeq import root
import numpy as np

from schemas.seeds.weight import Weight


import asyncio

seeds = []

for i in range(1,5):
    rand = i * np.random.random() * 10
    for j in range(1, 3):
        extra = rand * j
        seeds.append(extra)

for weight in seeds:
    data = Weight(weight)
    asyncio.run(create_max_weight(data))