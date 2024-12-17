import os

from dotenv import load_dotenv


load_dotenv() # looks in the ".env" file for env variables

API_KEY = os.getenv("NEWSAPI_KEY") #, default="demo"


