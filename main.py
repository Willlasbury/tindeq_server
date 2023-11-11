from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tindeq import TindeqHandler
from schemas.req.tindeqData import TindeqData
from schemas.res.weightRes import WeightRes

import os
from dotenv import load_dotenv
load_dotenv()

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
db_url = os.getenv('SUPABASE_URL')
print('db_url: ', db_url)
# todo: handle CORS
@app.get("/")
async def root():
    return {"message": "Hello World"}

# todo: add response schema
@app.post("/")
async def getTindeqData(data: TindeqData):
    try:
        res = tindeq.handleData(data.bytes)
        print(res)
        return res
    except:
        return 'error'
