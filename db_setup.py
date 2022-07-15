import sqlite3
from sqlite3 import Error

db_file = 'crimemap.db'
conn = None
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
    sql = """ CREATE TABLE IF NOT EXISTS crimes (
                                            id integer PRIMARY KEY AUTOINCREMENT,
                                            latitude FLOAT(10,6),
                                            longtitude FLOAT(10,6),
                                            date DATETIME,
                                            category VARCHAR(50),
                                            description VARCHAR(1000),
                                            updated_at TIMESTAMP
                                        ); """
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()


