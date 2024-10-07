## This script is used to query the database
## Starter portion of code from @porterjenkins on github
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

CONNECTION = os.getenv("TS_CONN_STRING") # paste connection string here or read from .env file
