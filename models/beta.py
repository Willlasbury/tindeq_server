from supabase import Client 

import os
from dotenv import load_dotenv
from supabase.lib.client_options import ClientOptions

class SupabaseWrapper(Client):
    def __init__(self, supabase_url: str, supabase_key: str, options: ClientOptions = ...):
        super().__init__(supabase_url, supabase_key, options)

