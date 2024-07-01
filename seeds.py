# from routes.weights import create_max_weight
# from routes.weights import delete_max_weights
from routes.grip_style import create_style
from routes.tindeq import root

from models.weight import Weight
from models.styles import Style

import asyncio

seeds = []

# for i in range(1,5):
#     rand = i * np.random.random() * 10
#     for j in range(3, 5):
#         extra = rand * j
#         seeds.append(round(extra,1))

# asyncio.run(delete_max_weights())

# for weight in seeds:
#     data = Weight(weight)
#     asyncio.run(create_max_weight(data))

# create all style options at once

styles = []

edge_sizes = [4, 6, 7, 8, 10, 12, 15, 20]
grips = ["full", "open", "half"]
hands = ["left", "right"]
finger = [True, False]

for i in edge_sizes:
    for j in grips:
        for k in hands:
            for l in finger:
                for m in finger:
                    for n in finger:
                        for o in finger:
                            styles.append(
                                {
                                    "edge_size": i,
                                    "grip": j,
                                    "hand": k,
                                    "index": l,
                                    "middle": m,
                                    "ring": n,
                                    "pinky": o,
                                }
                            )
for style in styles:
    data = Style(
        edge_size_mm=style.get("edge_size"),
        grip=style.get("grip"),
        hand=style.get("hand"),
        index=style.get("index"),
        middle=style.get("middle"),
        ring=style.get("ring"),
        pinky=style.get("pinky"),
    )
    asyncio.run(create_style(data))
