import requests
from requests import Response
import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")


class SupabaseReq:
    def __init__(self) -> None:
        self.url = url
        self.key = key

    def get(self, headers) -> Response:
        # return requests.get(f"{self.url}/{endpoint}", params=params, headers={"apiKey": self.key, **headers})
        res = requests.get(url="https://dkmvspmsglplyfthgrxb.supabase.co/rest/v1/max_pull?select=*", headers={"apiKey": self.key, **headers})
        return res

    def post(self, endpoint, json, headers):
        requests.post(f"{self.url}/{endpoint}", json=json, headers={"apiKey": self.key, **headers})
