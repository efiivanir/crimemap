import sqlite3
from sqlite3 import Error
import datetime
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(BASE_DIR, "crimemap.db")


class DBHelper:


    def add_crime(self, category, date, latitude, longtitude,description):
        try:
            conn = sqlite3.connect(db_file)
            query = "INSERT INTO crimes (category, date, latitude,longtitude, description) VALUES(?,?,?,?,?);"
            conn.cursor().execute(query, (category, date, latitude, longtitude,description))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def get_all_crimes(self):
        try:
            conn = sqlite3.connect(db_file)
            query = "SELECT latitude, longtitude, date, category,description FROM crimes; "
            # conn.cursor().execute(query)
            named_crimes = []
            a = list(conn.cursor().execute(query))
            for crime in a:
                named_crime = {
                    'latitude': crime[0],
                    'longitude': crime[1],
                    # 'date': datetime.datetime.strftime(crime[2], '%Y-%m-%d'),
                    'date': crime[2],
                    'category': crime[3],
                    'description': crime[4]
                }
                named_crimes.append(named_crime)
            return named_crimes
        finally:
            conn.close()
