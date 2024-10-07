
## This script is used to insert data into the database
## Starter portion of code from @porterjenkins on github
import os
import json
from dotenv import load_dotenv
from datasets import load_dataset
import pandas as pd

from recommender.utils import fast_pg_insert

load_dotenv()
CONNECTION = os.getenv("TS_CONN_STRING")

# TODO: Read the embedding files

# TODO: Read documents files

# HINT: In addition to the embedding and document files you likely need to load the raw data via the hugging face datasets library
ds = load_dataset("Whispering-GPT/lex-fridman-podcast")


# TODO: Insert into postgres
# HINT: use the recommender.utils.fast_pg_insert function to insert data into the database
# otherwise inserting the 800k documents will take a very, very long time
fast_pg_insert(df, CONNECTION, table_name, columns)
