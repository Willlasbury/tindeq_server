from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

class tindeqData(BaseModel):
    bytes: str

# todo: handle CORS
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def getTindeqData(data: tindeqData):
    try:
        print('data: ', data)
    except:
        print('some error')
    return 'hi'
