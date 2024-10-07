## This script is used to drop the tables in the database
## Starter portion of code from @porterjenkins on github

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

CONNECTION = os.getenv("TS_CONN_STRING") # paste connection string here or read from .env file

DROP_TABLE = "DROP TABLE podcast, podcast_segment"

with psycopg2.connect(CONNECTION) as conn:
    cursor = conn.cursor()
    cursor.execute(DROP_TABLE)
