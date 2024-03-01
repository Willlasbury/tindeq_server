import requests
from requests import Response
import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")


class SupabaseReq:
    def __init__(self, table=None) -> None:
        self.url = url
        self.key = key
        self.endpoint = f"rest/v1/{table}" if table else "/auth/v1/token"
        self.header = {"Content-Type": "application/json", "apikey": self.key}

    def _param_payload(self, params):
        return "&".join("%s=%s" % (k, v) for k, v in params.items())

    def _headers(self, headers: dict):
        return {**self.header, **headers}

    def _url(self):
        return f"{self.url}/{self.endpoint}"

    def get(self, headers, params):
        url = self._url()
        header = self._headers(headers)
        param_string = self._param_payload(params)
        res = requests.get(
            url=url,
            params=param_string,
            headers=header,
        )
        return res

    def post(self, endpoint, json, headers):
        requests.post(
            f"{self.url}/{endpoint}", json=json, headers={"apiKey": self.key, **headers}
        )
