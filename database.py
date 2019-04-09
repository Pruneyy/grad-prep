import sqlite3
from sqlite3 import Error
import os

def check_db():
    return os.path.isfile('data.db')

def create_db():
    """ Creates a new database if data.db does not exist in directory"""
    try:
        conn = sqlite3.connect("data.db")
        sql_create_responses_table = """CREATE TABLE IF NOT EXISTS responses (
                                            id integer PRIMARY KEY,
                                            question text,
                                            answer text
                                        );"""
        c = conn.cursor()
        c.execute(sql_create_responses_table)
    except Error as e:
        print(e)
    finally:
        conn.close()

def add_db(question, answer):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT Count(*) FROM responses")
    id = c.fetchone()[0]
    c.execute("INSERT INTO responses VALUES(?,?,?)", (id, question, answer,))
    conn.commit()
    return None

def query_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT question, answer FROM responses")
    responses = c.fetchall()
    return responses