import sqlite3
import time
import datetime
import random

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
                bill_id TEXT NOT NULL DEFAULT 'Empty',
                find_teacher TEXT NOT NULL DEFAULT 'Empty',
                referrer_code TEXT NOT NULL DEFAULT 'Empty',
                referral_types TEXT NOT NULL DEFAULT 'Empty',
                referrals INTEGER NOT NULL DEFAULT '0'
            )    
            """
            cursor.executescript(query)
            db.commit()
            # cursor.close()
            # db.close()
    
    # def create_db(self):
    #     with sqlite3.connect('users.db') as db:
    #         cursor = db.cursor()
    #         query = """CREATE TABLE IF NOT EXISTS groups_id(
    #             id INTEGER PRIMARY KEY,
    #             group_name TEXT,
    #             group_id TEXT)""" 
    
    #         cursor.executescript(query)
    #         db.commit()

    # values = [2378,'Egor','wyw']

    #записать массив в базу

    def write_in_db(self, path, users, values):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            query = f'INSERT INTO {users} (user_id, name, user_name) VALUES (?, ?, ?)'  
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
    def write_in_db_groups(self, path, users, values):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            query = f'INSERT INTO {users} (id, group_name, group_id) VALUES (?, ?, ?)'  
            try:
                cursor.execute(query,values)
                # return True
            except sqlite3.IntegrityError:
                # return False
                print('#SQLITE3 Primary key is not unique')
            finally:
                db.commit()

    #найти значени по id и названию колонки

    def find_value(self, path, users, id, column_name):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT {column_name} FROM {users} WHERE user_id = ?",[id])
            # db.commit()
            # print(cursor.fetchone()[0])
            return cursor.fetchone()[0]
            # db.commit()
            # cursor.close()
            # db.close()

    def check_ref_code(self, path, users, ref_id, column_name):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT {column_name} FROM {users} WHERE referrer_code = ?",[ref_id])
            # db.commit()
            # print(cursor.fetchone()[0])

            try:
                return cursor.fetchone()[0]
                # return True
            except TypeError:
                return 'Ваш код не верный\nПорпробуйте еще раз!'

    def check_ref_types(self, path, users, ref_types, column_name):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT {column_name} FROM {users} WHERE referral_types = ?",[ref_types])
            # db.commit()
            # print(cursor.fetchone()[0])
            return cursor.fetchone()[0]

            # db.commit()
            # cursor.close()
            # db.close()  

    #изменить значени по id и названию колонки



    def change_value(self, path, users, id, column_name, new_value):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE {users} SET {column_name} = '{new_value}' WHERE user_id = ?",[id])
            db.commit()
            # cursor.close()
            # db.close()

    def find_all(self,path, users,column_name):
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT {column_name} FROM {users}")
            return cursor.fetchall()



#add root

# database = Database()
# database.path = 'users.db'
# path = database.path
# database.change_value(path, 837095301, 'sub_format','Free')

# creat db

database = Database()
database.path = 'users.db'
path = database.path
database.create_db()



