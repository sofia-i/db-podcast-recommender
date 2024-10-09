## This script is used to query the database
## Starter portion of code from @porterjenkins on github
import os
import psycopg2
from dotenv import load_dotenv

def print_csv(cols, data):
    print(";".join(cols))
    for entry in data:
        print(";".join(map(str, entry)))

def print_markdown_table(cols, data, truncate=True, decimal_places=2):
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


def find_similar_segments(conn, input_segment_id, count, reverse=False):
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
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        field_names = [i[0] for i in cursor.description]
        data = cursor.fetchall()

    return field_names, data

def find_similar_episodes_to_seg(conn, input_segment_id, count):
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
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        field_names = [i[0] for i in cursor.description]
        data = cursor.fetchall()

    return field_names, data

def find_similar_episodes_to_ep(conn, ep_id, count):
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
    with psycopg2.connect(CONNECTION) as conn:
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
    cols3, data3 = find_similar_segments(CONNECTION, "48:551", count=5)
    print("Segments similar to 48:551:")
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
    
# TODO: exclude whole podcast episode?

q1()
print("\n\n")
q2()
print("\n\n")
q3()
print("\n\n")
q4()
print("\n\n")
q5()
print("\n\n")
q6()