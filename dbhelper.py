import sqlite3
from sqlite3 import Error
import datetime

db_file = 'crimemap.db'

class DBHelper:
    def get_all_inputs(self):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            # query = 'SELECT "description" FROM crimes;'
            query = 'SELECT description FROM crimes;'
            rows = list(conn.cursor().execute(query))
            #rows = conn.cursor().fetchall()
            return rows
        except Error as e:
            print(e)
        finally:
            conn.close()

    def add_input(self, data):
        try:
            conn = sqlite3.connect(db_file)
            query = "INSERT INTO crimes (description) VALUES('{}');".format(data)
            conn.cursor().execute(query)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def clear_all(self):
        try:
            conn = sqlite3.connect(db_file)
            query = "DELETE FROM crimes;"
            conn.cursor().execute(query)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

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
