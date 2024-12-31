import os
import falcon
import json

from wsgiref.simple_server import make_server
from supabase import create_client, Client
from dotenv import load_dotenv, dotenv_values

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Homepage:
    def on_get(self, req, res):
        data = {
            'message': 'Hello from Falcon',
            'github': 'https://github.com/marcomaza92/'
        }
        res.text = json.dumps(data)

class ToDo:
    def on_get(self, req, res):
        data = supabase.table("todos").select("*").execute()
        res.text = json.dumps(data.data)

# Resources

app = falcon.App()
homepage = Homepage()
todo = ToDo()

# Routes

app.add_route('/', homepage)
app.add_route('/todo', todo)