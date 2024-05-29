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

# used for filling out style table with all possible combos
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

    unique = supabase.table('style').select('*').match(style).execute()
    if unique.data == []:
        res = supabase.table('style').insert(style).execute()
        return res
 