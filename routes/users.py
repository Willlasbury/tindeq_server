from fastapi import APIRouter, HTTPException, status, Request
from supabase import create_client, Client

from schemas.res.users import User
from schemas.res.login import Login

import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")

supabase: Client = create_client(url, key)

router = APIRouter(prefix="/users")



@router.get("/token")
async def check_session_token(request: Request):
    access_token = request.headers.get("Authorization")
    refresh_token = request.headers.get("Refresh-Token")
    res = supabase.auth.set_session(access_token, refresh_token)
    if res.user:
        return res
    else: 
       raise HTTPException(status_code=404, detail="Could not refresh token")

# not working
# @router.get("")
# async def get_all_users():
#     res = supabase.auth.get_user()
#     if res.data == []:
#         raise HTTPException(status_code=404, detail="Could not find any data")
#     return res.data

@router.post("")
async def create_user(data:User):
    user = {
        "display_name": data.display_name,
        "email": data.email,
        "password": data.password,
    }

    res = supabase.auth.sign_up(user)
    return res

@router.post("/login")
async def create_user(data:Login):

    # res = supabase.auth.sign_in_with_password(user)
    res = supabase.auth.sign_in(email=data.email, password=data.password)
    return res
