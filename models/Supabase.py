import requests
from requests import Response
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("API_KEY")


class SupabaseReq:
    def __init__(self, table=None) -> None:
        self.url = supabase_url
        self.key = key
        self.auth_url = "auth/v1"
        self.rest_url = "rest/v1"

        # Reference endpoints from supabase-py
        # self.realtime_url = f"{supabase_url}/realtime/v1".replace("http", "ws")
        # self.auth_url = f"{supabase_url}/auth/v1"
        # self.storage_url = f"{supabase_url}/storage/v1"
        # self.functions_url = f"{supabase_url}/functions/v1"
        
        self.header = {"Content-Type": "application/json", "apikey": self.key, "Prefer": "return=minimal"}
    
    def _eq(self, params):
        return

    def _end_point(self, table):
        return f"rest/v1/{table}" 
    
    # create custom string to add as params since I am having trouble 
    #   with special character (e.g. *) returning as %... 
    def _param_payload(self, params): 
        return "&".join("%s=%s" % (k, v) for k, v in params.items())

    # add any headers other than the default
    def _headers(self, token, **kwargs):
        if kwargs.get('custom_headers') is not None:
            return {**self.header, **kwargs.get('custom_headers'), "Authorization":f"Bearer {token}"}
        else:
            return {**self.header, "Authorization":f"Bearer {token}"}

    # create the url path
    def _url(self, type, endpoint):
        return f"{self.url}/{type}/{endpoint}"

    def get_user_data(self, session_token):
        # param_string = self._param_payload({'grant_type':'password'})
        headers = self._headers(token=session_token)
        res = requests.get(url=self._url(self.auth_url, 'user'), headers=headers)
        return res.json()

    def get(self, table, session_token, params):
        url = self._url(self.rest_url, table)
        headers = self._headers(token=session_token)
        param_string = self._param_payload(params)
        res = requests.get(
            url=url,
            params=param_string,
            headers=headers,
        )
        return res.json()

    def get_where(self, table, session_token, params):
        url = self._url(self.rest_url, table)
        headers = self._headers(token=session_token)
        param_string = "&".join("%s=eq.%s" % (k, v) for k, v in params.items())
        res = requests.get(
            url=url,
            params=param_string,
            headers=headers,
        )
        return res
    
    def post(self, table, session_token, json):
        url = self._url(self.rest_url, table)
        headers = self._headers(token=session_token)
        res = requests.post(
            url=url,
            headers=headers,
            json=json
        )
        return res
