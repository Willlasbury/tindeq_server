from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tindeq import TindeqHandler

app = FastAPI()

origins = ["http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tindeq = TindeqHandler



# todo: handle CORS
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def getTindeqData(data):
    print(data)
    x = tindeq.handleData(data)
    print(x)
    return 
