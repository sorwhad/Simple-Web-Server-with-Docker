import mysql.connector
import sys 
import csv 
import os 


print("Connecting...")

config = {'host':'mydb', 
          'user': 'root',
          'password': 'root',
          'port': 3306, 
          'database': 'name_age'}


with mysql.connector.connect(**config) as connection:
    with connection.cursor() as cursor:
        with open("./data.csv", 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                name, age = row
                cursor.execute(f"INSERT INTO name_age_table (name, age) VALUES ('{name}', {age})")
    connection.commit()
        

with mysql.connector.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM name_age_table')
        results = {name: age for (name, age) in cursor}
         
print("Connected")
print(results)

