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

supa: Client = create_client(url, key)

sreq = SupabaseReq()

router = APIRouter(prefix="/max_pull")

# testing wrapper function to adjust headers


@router.get("/test")
async def get_max_pulls(request: Request):
    token = request.headers.get("Authorization")
    res = sreq.rpc(endpoint='test')
    print('res: ', res)
    return res


@router.get("/recent")
async def get_users_max_pull(request: Request):
    token = request.headers.get("Authorization")
    user_data = sreq.get_user_data(token)
    user_id = user_data.get('id')
    
    supa_dict = supa.table('max_pull').select('*').order('date', desc=True)

    max_pull_res = sreq.get(table='max_pull', supa_dict=supa_dict, session_token=token)
    return max_pull_res[0]

@router.get("/highest")
async def get_users_max_pull(request: Request) -> MaxWeightRes:
    token = request.headers.get("Authorization")
    supa_dict = supa.table('max_pull').select('weight_kg', 'style(*)')
    max_pull_res = sreq.get(table='max_pull', session_token=token, supa_dict=supa_dict)
    max = -1
    for i in range(len(max_pull_res)):
        el = max_pull_res[i]
        data = el if el.get('weight_kg') > max else data

    return data

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
    
    supa_dict = supa.table('style').select('*')

    for k,v in style.items():
        supa_dict.eq(f'{k}', v)

    style = sreq.get(table='style', session_token=token, supa_dict=supa_dict)
    style_id = style[0].get('id')

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
