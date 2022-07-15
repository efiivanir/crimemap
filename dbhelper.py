import sqlite3
from sqlite3 import Error

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
