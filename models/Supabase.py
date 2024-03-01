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

    def _headers(self, token, **kwargs):
        if kwargs.get('custom_headers') is not None:
            return {**self.header, **kwargs.get('custom_headers'), "Authorization":f"Bearer {token}"}
        else:
            return {**self.header, "Authorization":f"Bearer {token}"}

    def _url(self):
        return f"{self.url}/{self.endpoint}"

    def get(self, session_token, params):
        url = self._url()
        header = self._headers(token=session_token)
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
