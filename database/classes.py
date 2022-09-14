import sqlite3
import time
import datetime

# from core.find_group import find_group


class Database():

    path = 'users.db'

    # создание базы-данных
    def create_db(self):
        with sqlite3.connect('users.db') as db:
            cursor = db.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY,
                name TEXT,
                user_name TEXT,
                user_group TEXT NOT NULL DEFAULT 'None',
                sub_format TEXT NOT NULL DEFAULT 'Free',
                sub_expiration TEXT NOT NULL DEFAULT '2007.07.07',
                bill_id TEXT NOT NULL DEFAULT 'Empty'  
            )    
            """
            cursor.executescript(query)
            db.commit()
            # cursor.close()
            # db.close()
    

    # values = [2378,'Egor','wyw']

    #записать массив в базу

    def write_in_db(self, path, values):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            query = """
            INSERT INTO users (user_id, name, user_name) VALUES (?, ?, ?)  
            """
            try:
                cursor.execute(query,values)
                # return True
            except sqlite3.IntegrityError:
                # return False
                print('#SQLITE3 Primary key is not unique')
            finally:
                db.commit()
                # cursor.close()
                # db.close()

    #найти значени по id и названию колонки

    def find_value(self, path, id, column_name):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT {column_name} FROM users WHERE user_id = ?",[id])
            # db.commit()
            # print(cursor.fetchone()[0])
            return cursor.fetchone()[0]
            # db.commit()
            # cursor.close()
            # db.close()

    #изменить значени по id и названию колонки



    def change_value(self, path, id, column_name, new_value):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE users SET {column_name} = '{new_value}' WHERE user_id = ?",[id])
            db.commit()
            # cursor.close()
            # db.close()


#add root

# database = Database()
# database.path = 'users.db'
# path = database.path
# database.change_value(path, 837095301, 'sub_format','Free')

# creat db

# database = Database()
# database.path = 'users.db'
# path = database.path
# database.create_db()



