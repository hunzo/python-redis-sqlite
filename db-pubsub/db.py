import sqlite3
import logging

def create_db():
    try:
        with sqlite3.connect("db/db.sqlite") as con:
            sql_cmd = """
                CREATE TABLE person(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    cardid text,
                    studentname text,
                    studentid text,
                    studentaccount text,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            con.execute(sql_cmd)
            logging.warning('Create database success !!!')
    except Exception as e:
        logging.warning(f'Error (create_db) -> {e}')

def insert_db(params):
    try:
        with sqlite3.connect("db/db.sqlite") as con:
            sql_cmd = f"""
                INSERT INTO person(
                    cardid,
                    studentname,
                    studentid,
                    studentaccount
                ) values (?, ?, ?, ?)
            """
            con.execute(sql_cmd, params)
    except Exception as e:
        logging.warning(f'Error (insert_db) -> {e}')    

def select_db():
    try:
        with sqlite3.connect("db/db.sqlite") as con:
            sql_cmd = f"""
                SELECT
                id,
                studentname,
                studentid,
                studentaccount,
                cardid,
                datetime(timestamp, 'localtime')
                from 
                person
            """
            for row in con.execute(sql_cmd):
                logging.warning(row)

    except Exception as e:
        logging.warning(f'Error (select_db) -> {e}')    

def delete_db():
    try:
        with sqlite3.connect("db/db.sqlite") as con:
            sql_cmd = f"""
                DELETE FROM person WHERE name = 'user1'
            """
            con.execute(sql_cmd)

    except Exception as e:
        loggin.warning(f'Error (delete_db) -> {e}')    

def drop_table():
    try:
        with sqlite3.connect("db/db.sqlite") as con:
            sql_cmd = f"""
                DROP TABLE person
            """
            con.execute(sql_cmd)

    except Exception as e:
        loggin.warning(f'Error (drop_table) -> {e}')    
