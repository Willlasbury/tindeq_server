from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tindeq import TindeqHandler
from schemas.req.tindeqData import TindeqData
from schemas.res.weightRes import WeightRes
from schemas.req.weightData import Weight

import os
from dotenv import load_dotenv
load_dotenv()

from supabase import create_client, Client

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




@app.get("/tindeq")
async def root():
    return {"message": "Hello World"}

# todo: add response schema
@app.post("/tindeq")
async def getTindeqData(data: TindeqData):
    try:
        res = tindeq.handleData(data.bytes)
        return res
    except:
        return 'error'

# route for testing supabase connection
# ONLY WORKS WITH RLS DISABLED ON SUPABASE TABLE
@app.post("/measurement")
async def insert(data: Weight):
    value = {'weight':data.weight}
    url : str = os.getenv('SUPABASE_URL')
    key : str = os.getenv('API_KEY')
    supabase: Client = create_client(url, key)
    res = supabase.table('max_weight').insert(value).execute()
    return res


@app.post("/max_weight")
async def handle_max_weight(data: Weight):
    value = {'weight':data.weight}
    url : str = os.getenv('SUPABASE_URL')
    key : str = os.getenv('API_KEY')
    supabase: Client = create_client(url, key)
    res = supabase.table('max_weight').insert(value).execute()
    return res