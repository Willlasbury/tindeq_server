from fastapi import APIRouter, HTTPException, status, Request
from supabase import create_client, Client

from schemas.req.styleData import StyleData

import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")

supabase: Client = create_client(url, key)

router = APIRouter(prefix="/style")

@router.get("")
async def get_style():
    res = supabase.auth.get_style()
    if res.data == []:
        raise HTTPException(status_code=404, detail="Could not find any data")
    return res.data

@router.post("")
async def create_style(data:StyleData):
    style = {
        "edge_size_mm": data.edge_size_mm,
        "grip": data.grip,
        "hand": data.hand,
        "index": data.index,
        "middle": data.middle,
        "ring": data.ring,
        "pinky": data.pinky,
        }

    res = supabase.table('style').insert(style).execute()
    print(res)
    return res