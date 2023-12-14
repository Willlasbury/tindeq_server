from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, status
from supabase import create_client, Client

from schemas.res.users import User

import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")

supabase: Client = create_client(url, key)

router = APIRouter(prefix="/users")



@router.get("/test")
async def get_all_users():
    return {
        "message": "test success"
    }

@router.get("")
async def get_all_users():
    res = supabase.auth.get_user()
    if res.data == []:
        raise HTTPException(status_code=404, detail="Could not find any data")
    return res.data

@router.post("")
async def create_user(data:User):
    user = {
        "display_name": data.display_name,
        "email": data.email,
        "password": data.password,
    }
    res = supabase.auth.sign_up(user)
    return res