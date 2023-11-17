from fastapi import APIRouter, HTTPException, status
from supabase import create_client, Client

from schemas.req.weightData import Weight
from schemas.res.max_weight import MaxWeightRes

import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/weights")


# route for testing supabase connection
# ONLY WORKS WITH RLS DISABLED ON SUPABASE TABLE
@router.post("", status_code=status.HTTP_201_CREATED, response_model=MaxWeightRes)
async def handle_max_weight(data: Weight):
    value = {"weight": data.weight}

    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("API_KEY")

    supabase: Client = create_client(url, key)

    res = supabase.table("max_weight").insert(value).execute()

    # need to check what supabase errors look like
    if not res.data[0]:
        raise HTTPException(status_code=502, detail="Data not added to database")

    return res.data[0]
