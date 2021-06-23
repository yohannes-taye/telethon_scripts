#!/usr/bin/env python3
from sqlalchemy import *
import sqlite3
db = create_engine('sqlite:///astenagaj2.db')

db.echo = False  # Try changing this to True and see what happens

class DB: 
      def __init__(self, dbName):
            self.dbName = dbName
            self.conn = None 

      def createTables(self): 
            metadata = MetaData(self.db)
            self.users = Table('users', metadata,
                  Column('user_id', Integer, primary_key=True),
                  Column('name', String(40)),
                  Column('age', Integer),
                  Column('password', String),
            )
            self.resturant_table = Table('resturant', metadata, 
                  Column('id', Integer, primary_key=True, autoincrement=True), 
                  Column('name', String(40))      
            )
            self.menu_table = Table('menu', metadata, 
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('resturant_id', Integer),
                  Column('type', Integer),
                  Column('name', String(40))      
            )
            try: 
                  self.menu_table.create()
            except: 
                  print("Menu table aready exists")
            try: 
                  self.resturant_table.create() 
            except: 
                  print("Resturant table already exists")
            try: 
                  self.users.create()
            except: 
                  print("Users table already exists")

      def dropAllTable(self): 
            try:
                  self.users.drop(self.db) 
            except: 
                  print("Users table does not exist")

            try: 
                  self.resturant_table.drop(self.db)
            except: 
                  print("Resturant table does not exist")

            try: 
                  self.menu_table.drop(self.db)
            except:
                  print("Menu table does not exist")

      def populateUsersTable(self): 
            i.execute({'name': 'John', 'age': 42},
                  {'name': 'Susan', 'age': 57},
                  {'name': 'Carl', 'age': 33}) 
      def populateResturantTable(self):
             i.execute({'name': 'McDonald', 'age': 42},
                  {'name': 'KFC', 'age': 57},
                  {'name': 'Burger King', 'age': 33})  
            pass 
      def populateMenuTable(self): 
            pass 
      def populateTables(self): 
            self.populateUsersTable() 
            self.populateResturantTable() 
            self.populateMenuTable() 




i = resturant_table.insert()
i.execute({'name': 'LaliRanch-Bar'})

i = resturant_table.insert()
i.execute({'name': 'LaliRanch-Bar'})

s = menu_table.select()
rs = s.execute()

row = rs.fetchone()
print(f'Id: {row[0]}')
print(f'Name: {row["name"]}')
print(f'Age: {row.age}')
print(f'Password: {row[users.c.password]}')

for row in rs:
    print(f"{row.name} is {row.age} years old")

# class DB:
#       def __init__(self, dbName):
#             self.dbName = dbName
#             self.conn = None 
#       def createConnection(self): 
#             self.conn = sqlite3.connect(self.dbName)
#             return self.conn

#       def getConnection(self):
#             return self.conn if not self.conn == None else self.createConnection() 

#       def createTable(self, name, primaryFieldName, columns): 
#             try: 
#                   separator = ','
#                   columns = separator.join(columns)
#                   fullCommand= f'''
#                   CREATE TABLE {name} ({primaryFieldName} INTEGER PRIMARY KEY AUTOINCREMENT, {columns})            
#                   '''
#                   conn = self.getConnection() 
#                   conn.execute(fullCommand)
#                   conn.commit()
#             except: 
#                   print("Table already exists")
#       def insertToTable(self, tableName, columns, data):
#             separator = ','
#             columns = separator.join(columns)
#             data = separator.join(data)
#             fullCommand = f'''INSERT INTO {tableName} ({columns}) VALUES ({data})''' 
#             print(fullCommand)
#             conn = self.getConnection() 
#             conn.execute(fullCommand)


#       def closeConnection(self): 
#             conn.close()

# d = DB('astenagaj.db')
# d.createTable('asd', 'ad', ['name TEXT NOT NULL'])
# d.insertToTable('asd', ['name'], ['\'lali\''])

# conn.execute('''CREATE TABLE resturant
#          (id INTEGER PRIMARY KEY AUTOINCREMENT,
#          name TEXT NOT NULL);''')

# conn.execute

# conn.execute("INSERT INTO resturant (name) \
#       VALUES ('Paul')")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

# conn.commit()
# print("Records created successfully")
# conn.close()
# import sqlite3
# from contextlib import closing

# connection = sqlite3.connect("aquarium.db")
# cursor = connection.cursor()
# try: 
#     cursor.execute("CREATE TABLE resturant (id INTEGER AUTOINCREMENT, name TEXT")
# except: 
#     pass 
# cursor.execute("INSERT INTO resturant VALUES ('Macdonalds')")
# rows = cursor.execute("SELECT name FROM resturant").fetchall()


# # target_fish_name = "Jamie"
# # rows = cursor.execute(
# #     "SELECT name, species, tank_number FROM fish WHERE name = ?",
# #     (target_fish_name,),
# # ).fetchall()
# print(rows)


# #Modifying data 
# # new_tank_number = 2
# # moved_fish_name = "Sammy"
# # cursor.execute(
# #     "UPDATE fish SET tank_number = ? WHERE name = ?",
# #     (new_tank_number, moved_fish_name)
# # )