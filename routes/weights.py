from fastapi import APIRouter, HTTPException, status
from supabase import create_client, Client

from schemas.req.weightData import Weight
from schemas.res.max_weight import MaxWeightRes

import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")

supabase: Client = create_client(url, key)


router = APIRouter(prefix="/max_pull")


# ONLY WORKS WITH RLS DISABLED ON SUPABASE TABLE
@router.get("", response_model=list[MaxWeightRes])
async def get_max_pulls():
    res = supabase.table("max_pull").select("*").execute()
    if res.data == []:
        raise HTTPException(status_code=404, detail="Could not find any data") 
    return res.data


@router.post("", status_code=status.HTTP_201_CREATED, response_model=MaxWeightRes)
async def create_max_pull(data: Weight):
    value = {"weight": data.weight}

    res = supabase.table("max_pull").insert(value).execute()

    # need to check what supabase errors look like
    if res.data == []:
        raise HTTPException(status_code=502, detail="Data not added to database")

    return res.data[0]

# Delete this end point as soon as you want to store real data
@router.delete("")
async def delete_max_pulls():
    res = supabase.table('max_pull').delete().neq('id', 0).execute()
    return res