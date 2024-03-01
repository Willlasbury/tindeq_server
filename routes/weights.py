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
    res = requester.get(params={'select':'*'}, headers={"Authorization":f"Bearer {token}"})
    return res.json()

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
    # print('\ntest\n')
    token = request.headers.get("Authorization")
    user_data = supabase.auth.get_user(token)
    user_id = user_data.user.id
    style = supabase.table('style').select('*').match(style).execute()
    style_id = style.data[0].get('id')
    # if unique.data == []:
    #     style_data = supabase.table('style').insert(style).execute()
    # return token, supabase._auth_token
    # print('data: ', data)
    obj = {
        "user_id":user_id,
        "style_id": style_id,
        "weight_kg": data.weight
    }
    try:
        # supabase._auth_token = {'apiKey': key, 'Authorization': f"Bearer {token}"}
        # print('\nsupabase auth header: ', supabase._get_token_header(),"\n")
        res = supabase.table("max_pull").insert(obj).execute()
        # res = requests.post("https://dkmvspmsglplyfthgrxb.supabase.co/rest/v1/max_pull", json=obj, headers={'apiKey': key, 'Authorization': f"Bearer {token}"})
        return res
        # return {'message':"sucess"}
    except Exception as e:

        return {'message':"error"}
        # raise HTTPException(status_code=400, detail=e.message)
    

# Delete this end point as soon as you want to store real data
@router.delete("")
async def delete_max_pulls():
    res = supabase.table("max_pull").delete().neq("id", 0).execute()
    return res
