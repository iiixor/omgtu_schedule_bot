import sqlite3
import time
import datetime
import random
import psycopg2

# from core.find_group import find_group
 

class Database():

    host = "ec2-44-207-126-176.compute-1.amazonaws.com"
    user = "wsspajnyulyfst"
    db_name = "users"

    path = 'users.db'

    # создание базы-данных

    def check_version(self):
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)

        with connection.cursor() as cursor:
            cursor.execute('SELECT version();')
            print(f'Server version  {cursor.fetchone()}')

    def create_db(self):

        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)
        
        # connection = psycopg2.connect(host=host,user=user,database=db_name, password = passwod)
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE users(
                        user_id serial PRIMARY KEY,
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
                    );
                    """)
                connection.commit()
                print('[INFO] PostgreSQL database was created successfully')

            # with sqlite3.connect('users.db') as db:
            #     cursor = db.cursor()
            #     query = """
            #     CREATE TABLE IF NOT EXISTS users(
            #         user_id INTEGER PRIMARY KEY,
            #         name TEXT,
            #         user_name TEXT,
            #         user_group TEXT NOT NULL DEFAULT 'None',
            #         sub_format TEXT NOT NULL DEFAULT 'Free',
            #         sub_expiration TEXT NOT NULL DEFAULT '2007.07.07',
            #         bill_id TEXT NOT NULL DEFAULT 'Empty',
            #         find_teacher TEXT NOT NULL DEFAULT 'Empty',
            #         referrer_code TEXT NOT NULL DEFAULT 'Empty',
            #         referral_types TEXT NOT NULL DEFAULT 'Empty',
            #         referrals INTEGER NOT NULL DEFAULT '0'
            #     )    
            #     """
            #     cursor.executescript(query)
            #     db.commit()
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

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

    def drop_db(self):
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    DROP TABLE users;
                """)
                connection.commit()
                print('[INFO] PostgreSQL database was droped successfully')

        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

        

    def write_in_db(self,values):
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)
        # print(f'{values[0]}, {values[1]}, {values[2]}')
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO users (user_id, name, user_name) VALUES ({values[0]}, '{values[1]}', '{values[2]}');")
                connection.commit()
                print('[INFO] PostgreSQL user was added')                                                                                               
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")







        # with sqlite3.connect(path) as db:
        #     cursor = db.cursor()
        #     query = f'INSERT INTO {users} (user_id, name, user_name) VALUES (?, ?, ?)'  
        #     try:
        #         cursor.execute(query,values)
        #         # return True
        #     except sqlite3.IntegrityError:
        #         # return False
        #         print('#SQLITE3 Primary key is not unique')
        #     finally:
        #         db.commit()
        #         # cursor.close()
        #         # db.close()
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
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)
        # print(f'{values[0]}, {values[1]}, {values[2]}')
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {column_name} FROM {users} WHERE user_id = {id};")
                connection.commit()
                print(f'[INFO] PostgreSQL {column_name} was found')  
                return cursor.fetchone()[0]
                connection.commit()
                print('[INFO] PostgreSQL user was added')                                                                                               
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")



        # with sqlite3.connect(path) as db:
        #     cursor = db.cursor()
        #     cursor.execute(f"SELECT {column_name} FROM {users} WHERE user_id = ?",[id])
        #     # db.commit()
        #     # print(cursor.fetchone()[0])
        #     return cursor.fetchone()[0]
        #     # db.commit()
        #     # cursor.close()
        #     # db.close()

    def check_ref_code(self, path, users, ref_id, column_name):
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {column_name} FROM {users} WHERE referrer_code = {ref_id};")
                connection.commit()
                print(f'[INFO] PostgreSQL {column_name} was found')  
                try:
                    return cursor.fetchone()[0]
                    connection.commit()
                except TypeError:
                    return 'Ваш код не верный\nПорпробуйте еще раз!'                                                                                            
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")
        # with sqlite3.connect(path) as db:
        #     cursor = db.cursor()
        #     cursor.execute(f"SELECT {column_name} FROM {users} WHERE referrer_code = ?",[ref_id])
        #     # db.commit()
        #     # print(cursor.fetchone()[0])

        #     try:
        #         return cursor.fetchone()[0]
        #         # return True
        #     except TypeError:
        #         return 'Ваш код не верный\nПорпробуйте еще раз!'

    def check_ref_types(self, path, users, ref_types, column_name):
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)

        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {column_name} FROM {users} WHERE referrer_code = {ref_types};")
                connection.commit()
                print(f'[INFO] PostgreSQL {column_name} was found')  
                try:
                    return cursor.fetchone()[0]
                    connection.commit()
                except TypeError:
                    return 'Ваш код не верный\nПорпробуйте еще раз!'                                                                                            
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

        # with sqlite3.connect(path) as db:
        #     cursor = db.cursor()
        #     cursor.execute(f"SELECT {column_name} FROM {users} WHERE referral_types = ?",[ref_types])
        #     # db.commit()
        #     # print(cursor.fetchone()[0])
        #     return cursor.fetchone()[0]

            # db.commit()
            # cursor.close()
            # db.close()  

    #изменить значени по id и названию колонки



    def change_value(self, path, users, id, column_name, new_value):
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)

        try:
            with connection.cursor() as cursor:
                if isinstance(new_value,int):
                    cursor.execute(f"UPDATE {users} SET {column_name} = {new_value} WHERE user_id = {id};")
                else:
                    cursor.execute(f"UPDATE {users} SET {column_name} = '{new_value}' WHERE user_id = {id};")
                connection.commit()
                print(f'[INFO] PostgreSQL {column_name} was changed')                                                                                             
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")




        # with sqlite3.connect(path) as db:
        #     cursor = db.cursor()
        #     cursor.execute(f"UPDATE {users} SET {column_name} = '{new_value}' WHERE user_id = ?",[id])
        #     db.commit()
            # cursor.close()
            # db.close()

    def find_all(self,path, users,column_name):
        host = "ec2-44-207-126-176.compute-1.amazonaws.com"
        user = "wsspajnyulyfst"
        port = '5432'
        db_name = "d60c65fs9q4fgl"
        password = "f9ac0de57950538e5d97d2bc9a3c35e8692008e5931aea46dd0de707628216f8"

        connection = psycopg2.connect(
                host=host,
                user=user,
                database=db_name, 
                password = password,
                port = port)

        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {column_name} FROM {users}")
                connection.commit()
                print(f'[INFO] PostgreSQL {column_name} was found') 
                return cursor.fetchall()                                                                                            
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL")
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

        # with sqlite3.connect(path) as db:
        #     cursor = db.cursor()
        #     cursor.execute(f"SELECT {column_name} FROM {users}")
        #     return cursor.fetchall()



#add root

# database = Database()
# database.path = 'users.db'
# path = database.path
# database.change_value(path, 837095301, 'sub_format','Free')

# creat db

database = Database()
# database.check_version()
# database.drop_db()
# database.create_db()
# database.write_in_db([83777,'wywdelpy','egor'])




