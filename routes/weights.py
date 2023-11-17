from fastapi import APIRouter
from supabase import create_client, Client

from schemas.req.weightData import Weight

import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(prefix='/weights')

# route for testing supabase connection
# ONLY WORKS WITH RLS DISABLED ON SUPABASE TABLE
@router.post("/test")
async def insert(data: Weight):
    value = {'weight':data.weight}
    url : str = os.getenv('SUPABASE_URL')
    key : str = os.getenv('API_KEY')
    supabase: Client = create_client(url, key)
    res = supabase.table('max_weight').insert(value).execute()
    return res


@router.post("")
async def handle_max_weight(data: Weight):
    value = {'weight':data.weight}
    url : str = os.getenv('SUPABASE_URL')
    key : str = os.getenv('API_KEY')
    supabase: Client = create_client(url, key)
    res = supabase.table('max_weight').insert(value).execute()
    return res