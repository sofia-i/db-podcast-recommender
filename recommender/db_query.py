## This script is used to query the database
## Starter portion of code from @porterjenkins on github
import os
import psycopg2
from dotenv import load_dotenv

def print_csv(cols, data):
    """
        Print column names and data as csv, with ; as the separator
    """
    print(";".join(cols))
    for entry in data:
        print(";".join(map(str, entry)))

def print_markdown_table(cols, data, truncate=True, decimal_places=3):
    """
        Print data in the format of a markdown table
        With cols as headers
        If truncate, round float values to `decimal_places` number of decimal places
    """
    # header titles
    print("|", " | ".join(cols), "|")
    # header underline
    header_underline = "| "
    for i in range(len(cols)):
        header_underline += " --- |"
    print(header_underline)
    # data rows
    for entry in data:
        if truncate:
            datastrs = [(f"%.{decimal_places}f" % val) if isinstance(val, float) else val for val in entry]
        else:
            datastrs = map(str, entry)
        datastrs = [s.replace("|", "&#124;") for s in datastrs]
        print("|", " | ".join(datastrs), "|")


def find_similar_segments(conn_str, input_segment_id, count, reverse=False):
    """
        Find `count` similar segments to the segment with id `input_segment_id`
        If reverse, find most dissimilar segments instead of most similar.
    """

    query = f"""
    SELECT i.title as "Podcast name", i.id as "Segment ID", 
            i.content as "Segment raw text", i.start_time as "Start time", 
            i.end_time as "Stop time", i.dist as "Embedding distance"
    FROM 
        (
        SELECT p.title, ps.id, ps.content, ps.start_time, ps.end_time, 
            ps.embedding <->
                (SELECT embedding FROM podcast_segment 
                WHERE id='{input_segment_id}') as dist
        FROM 
            (
            SELECT *
            FROM podcast_segment
            WHERE id != '{input_segment_id}'
            ) as ps
        INNER JOIN podcast as p
        ON p.id = ps.podcast_id
        ) as i
    ORDER BY i.dist {"DESC" if reverse else "ASC"}
    LIMIT {count};
    """

    data = None
    with psycopg2.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        field_names = [i[0] for i in cursor.description]
        data = cursor.fetchall()

    return field_names, data

def find_similar_episodes_to_seg(conn_str, input_segment_id, count):
    """
        Find `count` similar episodes to the segment with id `input_segment_id`
    """

    # NOTE: assuming no two episode titles are the same
    query = f"""
    SELECT i.title as "Podcast title", i.dist as "Embedding Distance"
    FROM
        (SELECT p.title, AVG(embedding) <->
            (SELECT embedding FROM podcast_segment
            WHERE id='{input_segment_id}') as dist
        FROM 
            (SELECT * FROM podcast_segment
            WHERE podcast_id !=
                (SELECT podcast_id
                FROM podcast_segment
                WHERE id = '{input_segment_id}')
            ) as ps
        INNER JOIN podcast as p
        ON p.id = ps.podcast_id
        GROUP BY p.title
        ) as i
    ORDER BY i.dist
    LIMIT {count};
    """

    data = None
    with psycopg2.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        field_names = [i[0] for i in cursor.description]
        data = cursor.fetchall()

    return field_names, data

def find_similar_episodes_to_ep(conn_str, ep_id, count):
    """
        Find `count` similar episodes to the podcast episode with id `ep_id`
    """

    query = f"""
    SELECT i.title as "Podcast title", i.dist as "Embedding Distance"
    FROM
        (SELECT p.title, AVG(embedding) <->
            (SELECT AVG(embedding)
            FROM podcast_segment
            INNER JOIN podcast
            ON podcast_id = podcast.id
            WHERE podcast_id='{ep_id}'
            GROUP BY podcast_id) as dist
        FROM 
            (SELECT * FROM podcast_segment
            WHERE podcast_id != '{ep_id}'
            ) as ps
        INNER JOIN podcast as p
        ON p.id = ps.podcast_id
        GROUP BY p.title
        ) as i
    ORDER BY i.dist
    LIMIT {count};
    """

    data = None
    with psycopg2.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        field_names = [i[0] for i in cursor.description]
        data = cursor.fetchall()

    return field_names, data

load_dotenv()

CONNECTION = os.getenv("TS_CONN_STRING") # paste connection string here or read from .env file

def q1():
    cols1, data1 = find_similar_segments(CONNECTION, "267:476", count=5)
    print("Segments similar to 267:476:")
    print()
    print_markdown_table(cols1, data1)

def q2():
    cols2, data2 = find_similar_segments(CONNECTION, "267:476", count=5, reverse=True)
    print("Segments dissimilar to 267:476:")
    print()
    print_markdown_table(cols2, data2)

def q3():
    cols3, data3 = find_similar_segments(CONNECTION, "48:511", count=5)
    print("Segments similar to 48:511:")
    print()
    print_markdown_table(cols3, data3)

def q4():
    cols4, data4 = find_similar_segments(CONNECTION, "51:56", count=5)
    print("Segments similar to 51:56:")
    print()
    print_markdown_table(cols4, data4)

def q5():
    for seg_id in ["267:476", "48:511", "51:56"]:
        cols, data = find_similar_episodes_to_seg(CONNECTION, seg_id, 5)
        print()
        print("Episodes similar to segment", seg_id)
        print()
        print_markdown_table(cols, data)
        print()

def q6():
    ep_id = "VeH7qKZr0WI"
    cols6, data6 = find_similar_episodes_to_ep(CONNECTION, ep_id, 5)
    print("Episodes similar to episode", ep_id)
    print()
    print_markdown_table(cols6, data6)
    
# TODO: exclude whole podcast episode when querying by segment?

def all_qs():
    print("~~~~~~~~~~~~~Q1~~~~~~~~~~~~~")
    q1()
    print("\n\n")
    print("~~~~~~~~~~~~~Q2~~~~~~~~~~~~~")
    q2()
    print("\n\n")
    print("~~~~~~~~~~~~~Q3~~~~~~~~~~~~~")
    q3()
    print("\n\n")
    print("~~~~~~~~~~~~~Q4~~~~~~~~~~~~~")
    q4()
    print("\n\n")
    print("~~~~~~~~~~~~~Q5~~~~~~~~~~~~~")
    q5()
    print("\n\n")
    print("~~~~~~~~~~~~~Q6~~~~~~~~~~~~~")
    q6()

all_qs()