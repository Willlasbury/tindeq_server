from datetime import datetime
from supabase import Client, create_client
from fastapi import APIRouter, HTTPException, status, Request
from models.Supabase import SupabaseReq
from schemas.req.weightData import WeightData
from schemas.res.max_weight import MaxWeightRes

import os
from dotenv import load_dotenv


load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")

sreq = SupabaseReq()

router = APIRouter(prefix="/max_pull")

# testing wrapper function to adjust headers


# ONLY WORKS WITH RLS DISABLED ON SUPABASE TABLE
@router.get("")
async def get_max_pulls(request: Request):
    supa: Client = create_client(url, key)
    res = supa.table('max_pull').select('weight_kg, style(grip)').eq('weight_kg', 100.02)
    param_string = res.__dict__.get('params')
    token = request.headers.get("Authorization")
    res = sreq.get(table='max_pull', params=param_string, session_token=token)
    return res


@router.get("/recent")
async def get_users_max_pull(request: Request):
    token = request.headers.get("Authorization")
    user_data = sreq.get_user_data(token)
    user_id = user_data.get('id')
    params = {
        'user_id':user_id,
    }
    max_pull_res = sreq.get_where(table='max_pull', params=params, session_token=token)
    max_pull_data = max_pull_res.json()
    return max_pull_data[-1]

@router.get("/highest")
async def get_users_max_pull(request: Request):
    token = request.headers.get("Authorization")
    user_data = sreq.get_user_data(token)
    user_id = user_data.get('id')
    params = {
        'user_id':user_id,
    }

    max_pull_res = sreq.get_where(table='max_pull', params=params, session_token=token)
    max_pull_data = max_pull_res.json()

    #filter through for max
    max = max_pull_data[0].get('weight_kg')
    for i in max_pull_data:
        weight = i.get('weight_kg')
        if weight > max:
            max = weight


    return {'max_weight_kg': max}

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
    user_data = sreq.get_user_data(token)
    user_id = user_data.get("id")
    # get style id
    style_res = sreq.get_where(table='style', session_token=token, params=style)
    print('style_res: ', style_res)
    style_id = style_res[0].get('id')
        
    obj = {
        "user_id":user_id,
        "style_id": style_id,
        "weight_kg": data.weight,
        "date": str(datetime.now())
    }
    try:
        res = sreq.post(table='max_pull', session_token=token, json=obj)
        return res
    except Exception as e:
        print('error: ', e)
        raise HTTPException(status_code=400, detail=e)
