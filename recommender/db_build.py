## This script is used to create the tables in the database
## Starter portion of code from @porterjenkins on github

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

CONNECTION = os.getenv("TS_CONN_STRING") # paste connection string here or read from .env file

# need to run this to enable vector data type
CREATE_EXTENSION = "CREATE EXTENSION vector"

# TODO: Add create table statement
CREATE_PODCAST_TABLE = """
CREATE TABLE podcast (
    id      INT PRIMARY KEY,
    title   TEXT
);
"""
# TODO: Add create table statement
CREATE_SEGMENT_TABLE = """
CREATE TABLE podcast_segment(
    id          INT PRIMARY KEY,
    start_time  TIME,
    end_time    TIME,
    content     TEXT,
    embedding   vector(128),
    podcast_id  INT,
    FOREIGN KEY (podcast_id) REFERENCES podcast(id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);
"""

conn = psycopg2.connect(CONNECTION)
# TODO: Create tables with psycopg2 (example: https://www.geeksforgeeks.org/executing-sql-query-with-psycopg2-in-python/)
with psycopg2.connect(CONNECTION) as conn:
    cursor = conn.cursor()
    cursor.execute(CREATE_EXTENSION)
    cursor.execute(CREATE_PODCAST_TABLE)
    cursor.execute(CREATE_SEGMENT_TABLE)
