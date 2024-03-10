from datetime import datetime

from fastapi import APIRouter, HTTPException, status, Request
from supabase import create_client, Client 
from models.Supabase import SupabaseReq
from schemas.req.weightData import WeightData
from schemas.res.max_weight import MaxWeightRes

import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")

supabase: Client = create_client(url, key)
requester = SupabaseReq(table='max_pull')

router = APIRouter(prefix="/max_pull")

# ONLY WORKS WITH RLS DISABLED ON SUPABASE TABLE
@router.get("")
async def get_max_pulls(request: Request):
    token = request.headers.get("Authorization")
    res = requester.get(table='max_pull', params={'select':'*'}, session_token=token)
    return res

# removed res modal remember to put back in
@router.post("", status_code=status.HTTP_201_CREATED)
async def create_max_pull(
    data:WeightData,
    request: Request,
):
    style = {
        "edge_size_mm": data.style.edge_size_mm,
        "grip": data.style.grip,
        "hand": data.style.hand,
        "index": data.style.index,
        "middle": data.style.middle,
        "ring": data.style.ring,
        "pinky": data.style.pinky,
        }
    
    token = request.headers.get("Authorization")

    # get user data
    user_data = requester.get_user_data(token)
    user_id = user_data.get("id")
    # get style id
    style_res = requester.get_where(table='style', session_token=token, params=style)
    style_data = style_res.json()
    style_id = style_data[0].get('id')
        
    obj = {
        "user_id":user_id,
        "style_id": style_id,
        "weight_kg": data.weight,
        "date": str(datetime.now())
    }
    try:
        res = requester.post(table='max_pull', session_token=token, json=obj)
        return res
    except Exception as e:
        print('error: ', e)
        raise HTTPException(status_code=400, detail=e)
