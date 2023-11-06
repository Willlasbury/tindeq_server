from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tindeq import TindeqHandler
from schemas.req.tindeqData import tindeqData
from schemas.res.weightRes import weightData

app = FastAPI()

origins = ["http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tindeq = TindeqHandler()


# todo: handle CORS
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def getTindeqData(data: tindeqData):
    try:
        res = tindeq.handleData(data.bytes)
        
        return res
    except:
        return 'error'
