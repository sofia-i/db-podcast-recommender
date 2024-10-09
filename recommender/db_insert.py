
## This script is used to insert data into the database
## Starter portion of code from @porterjenkins on github
import os
import json
from dotenv import load_dotenv
from datasets import load_dataset
import pandas as pd
import zipfile
from tqdm import tqdm

from utils import fast_pg_insert

load_dotenv()
CONNECTION = os.getenv("TS_CONN_STRING")

podcast_data = {}
segment_data = {}

# segment id: "custom_id" field
# Segment Data (id, start_time, end_time, content, embedding, podcast_id)
# Podcast Data (id, title)

# TODO: Read the embedding files
with zipfile.ZipFile('data/embedding.zip', 'r') as embed_archive:
   for name in tqdm(embed_archive.namelist()):
       with embed_archive.open(name) as embed:
           for line in embed:
                json_line = json.loads(line)
                id = json_line['custom_id']
                embedding = json_line['response']['body']['data'][0]['embedding']

                segment_data[id] = {
                    'embedding': embedding
                }

# TODO: Read documents files
with zipfile.ZipFile('data/documents.zip', 'r') as doc_archive:
   for name in tqdm(doc_archive.namelist()):
       with doc_archive.open(name) as doc:
           for line in doc:
                json_line = json.loads(line)
                id = json_line['custom_id']
                start_time = json_line['body']['metadata']['start_time']
                end_time = json_line['body']['metadata']['stop_time']
                content = json_line['body']['input']
                title = json_line['body']['metadata']['title']
                podcast_id = json_line['body']['metadata']['podcast_id']

                if podcast_id not in podcast_data:
                    podcast_data[podcast_id] = {
                        'id': podcast_id,
                        'title': title
                    }

                if id not in segment_data:
                    raise Exception("missing segment id " + id)
                
                segment_data[id]['id'] = id
                segment_data[id]['start_time'] = start_time
                segment_data[id]['end_time'] = end_time
                segment_data[id]['content'] = content
                segment_data[id]['podcast_id'] = podcast_id

# HINT: In addition to the embedding and document files you likely need to load the raw data via the hugging face datasets library
# TODO: WHY??
# ds = load_dataset("Whispering-GPT/lex-fridman-podcast")


# TODO: Insert into postgres
# HINT: use the recommender.utils.fast_pg_insert function to insert data into the database
# otherwise inserting the 800k documents will take a very, very long time
podcast_df = pd.DataFrame(podcast_data.values())
segment_df = pd.DataFrame(segment_data.values())

fast_pg_insert(podcast_df, CONNECTION, 'podcast', podcast_df.columns)
fast_pg_insert(segment_df, CONNECTION, 'podcast_segment', segment_df.columns)
